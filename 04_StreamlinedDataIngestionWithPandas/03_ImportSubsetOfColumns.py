# Create list of columns to use
cols = ____

# Create dataframe from csv using only selected columns
data = ____("vt_tax_data_2016.csv", ____)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())
