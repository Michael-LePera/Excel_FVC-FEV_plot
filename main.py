import sys

from modules.create_dp import excel_to_json
from modules.get_info import get_info
from modules.create_plot import create_plot

if __name__ == '__main__':
    args = sys.argv
    if 'dp' in args:
        excel_to_json(
            fname=f'{args[2]}.xlsx',
            sheetname= args[3],
            HEADINGS_ROW=3,
            gender_col=1,
            age_col=3,
            FVC_col=19,
            FEV_col=20,
            ENTRIES=366,
            heading_spacing=1
        )
    elif 'plot' in args:
        data = get_info('data_points.json')
        create_plot(data)