# Create dict specifying that 0s in zipcode are NA values
# Note that this is a bit of a hack, but it works
# The column is called 'zipcode' and must be written in quotes
null_values = {'zipcode': 0}

# Load csv using na_values keyword argument, which specifies the values to be treated as NA
data = pd.read_csv("vt_tax_data_2016.csv", na_values=null_values)

# View rows with NA ZIP codes by calling the isin() method
print(data[data.zipcode.isna()])
