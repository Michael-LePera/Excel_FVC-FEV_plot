import os
import openpyxl as opx 
import json


def excel_to_json(fname, sheetname, HEADINGS_ROW, gender_col, age_col, FVC_col, FEV_col, ENTRIES, heading_spacing):
    wb = opx.load_workbook(os.path.join('data',fname))
    ws = wb[sheetname]

    data_points = {
        "male":{
            "18-29":{"FVC":[], "FEV":[]},
            "30-39":{"FVC":[], "FEV":[]}
        },
        "female":{
            "18-29":{"FVC":[], "FEV":[]},
            "30-39":{"FVC":[], "FEV":[]}
        }
    }

    for row in range(HEADINGS_ROW + 1 + heading_spacing, ENTRIES):
        values = [ws.cell(row=row, column=x).value for x in [gender_col, age_col, FVC_col, FEV_col]]
        if None not in values:
            # print(values)
            match values[0]:
                case 'M':
                    if  18 <= values[1] <= 29:
                        data_points["male"]["18-29"]["FVC"].append(values[2])
                        data_points["male"]["18-29"]["FEV"].append(values[3])
                    elif 30 <= values[1] <= 39:
                        data_points["male"]["30-39"]["FVC"].append(values[2])
                        data_points["male"]["30-39"]["FEV"].append(values[3])
                case 'F':
                    if  18 <= values[1] <= 29:
                        data_points["female"]["18-29"]["FVC"].append(values[2])
                        data_points["female"]["18-29"]["FEV"].append(values[3])
                    elif 30 <= values[1] <= 39:
                        data_points["female"]["30-39"]["FVC"].append(values[2])
                        data_points["female"]["30-39"]["FEV"].append(values[3])

    with open('data_points.json', 'w') as outfile:
        json.dump(data_points, outfile, indent=4)

    wb.close()