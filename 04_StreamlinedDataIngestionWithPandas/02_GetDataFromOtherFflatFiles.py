# Import pandas with the alias pd
____

# Load TSV using the sep keyword argument to set delimiter
data = ____(____, ____)

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()
