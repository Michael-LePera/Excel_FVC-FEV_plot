import numpy as np
import json
import math

def reject_outliers(data, m = 3.):
    data = np.array(data)
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    data = data[s<m]
    return data.tolist()

def calc_mean(data):
    n = len(data)
    mean = sum(data) / n
    return mean, n


def variance(data, mean='',n='', ddof=0):
    if mean == '':
        mean, n = calc_mean(data)

    return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
    var = variance(data, ddof=1)
    std_dev = math.sqrt(var)
    return std_dev


def info(dp):
    mean, _ = calc_mean(dp)
    st_dev = stdev(dp)
    return st_dev, mean

def get_info(fname):

    with open(fname) as f:
        dp = json.load(f)

    output = []
    for gender in dp:
        for age_group in dp[gender]:
            for c_type in dp[gender][age_group]:
                data = dp[gender][age_group][c_type]
                data = reject_outliers(data)
                output.append([gender, age_group, c_type, data, info(data)])

    return output
