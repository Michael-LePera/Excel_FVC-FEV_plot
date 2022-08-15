# Excel_FVC-FEV_plot

## How to use
1. Download (right side of page)
2. Put into its own folder
3. make a new folder called 'data'
4. in the data folder add the excel sheet (rename to something short as you will need to type it later)

5. open a terminal in the directory with the .exe
6. `main <operation> <args>` run the file with arguments, operations include 'dp' for creating a datapoint file (required) and 'plot' for create graphs
- `dp <filename (excl. file extension)> <sheetname>`
- `plot <gender> <age_range> <type (FVC, FEV)>`
- Ex. `main plot male 18-29 FEV`
