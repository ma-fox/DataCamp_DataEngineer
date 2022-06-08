# Try to import the file vt_tax_data_2016_corrupt.csv without any keyword arguments.

try:
    # Import the CSV without any keyword arguments
    data = pd.read_csv('vt_tax_data_2016_corrupt.csv')

    # View first 5 records
    print(data.head())

except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")

# Import vt_tax_data_2016_corrupt.csv with the error_bad_lines parameter set to skip bad records.

try:
    # Import CSV with error_bad_lines set to skip bad records
    data = pd.read_csv("vt_tax_data_2016_corrupt.csv", error_bad_lines=False)

    # View first 5 records
    print(data.head())

except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")

# Update the import with the warn_bad_lines parameter set to issue a warning whenever a bad record is skipped.

try:
    # Set warn_bad_lines to issue warnings about bad records
    data = pd.read_csv("vt_tax_data_2016_corrupt.csv",
                       error_bad_lines=False,
                       warn_bad_lines=True)

    # View first 5 records
    print(data.head())

except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")
