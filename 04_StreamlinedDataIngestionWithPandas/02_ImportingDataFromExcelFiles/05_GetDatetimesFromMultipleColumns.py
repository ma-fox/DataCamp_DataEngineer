# Get datetimes from multiple columns

# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ____}

# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx", ____)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())
