from math import floor
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
import sys

def create_plot(all_data):
    args = sys.argv
    data = ''
    for d in all_data:
        c = 0
        for arg in args[2:]:
            if arg in d:
                c += 1
        if c == 3:
            data = d

    if data != '':
        plt.figure(figsize=(16, 9))
        sample = np.sort(np.array(data[3]))

        title = f'{data[0].upper()} {data[1]} {data[2].upper()}'
        
        
        std = data[4][0]
        mu = data[4][1]
        probabilities = norm.pdf(sample, mu, std)

        plt.plot(sample, probabilities, label=f"$\mu={mu}$\n$\sigma={std}$\n")
            
        
        plt.legend()
        plt.title(title)
        # plt.xlabel("Value")
        plt.ylabel("Probability")

        
        # Hide x ticks and labels
        plt.xticks(ticks=[],labels=[])


        aol = 5
        for i in range(aol):
            x = mu + (floor(aol/2) - i)*std
            plt.axvline(x, ls='--', color='black')
            text = str(floor(aol/2) - i + 1) + 'σ' if floor(aol/2) - i != 0 else 'µ'
            plt.text(x,0,text,rotation=0)

        plt.text(mu,-5,text,rotation=0)
        plt.show()

