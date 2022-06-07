# Import a file in chunks

# Create dataframe of next 500 rows with labeled columns
col_names = list(vt_data_first500)

vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv",
                              nrows=500,
                              skiprows=500,
                              header=None,
                              names=col_names)

# nrow = number of rows to read
# skiprows = number of rows to skip
# header = None to skip header, since pandas itself will otherwise create a wrong header
# names = list of column names, defined above in col_names

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())
