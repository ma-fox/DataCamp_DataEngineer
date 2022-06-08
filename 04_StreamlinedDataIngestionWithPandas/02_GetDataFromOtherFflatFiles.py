# Get data from other flat files

# Import pandas with the alias pd
import pandas as pd

# Import Matplotlib with the alias plt
from matplotlib import pyplot as plt


# Load TSV using the sep keyword argument to set delimiter
# TSV is tab separated values, so we use sep='\t'
data = pd.read_csv("vt_tax_data_2016.tsv", sep="\t")

# Plot the total number of tax returns by income group
# groupby() is a method of DataFrame, it groups by a column
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()
