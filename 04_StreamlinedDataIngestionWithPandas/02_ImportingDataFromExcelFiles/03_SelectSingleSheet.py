# Create a dataframe from the second workbook sheet by passing the sheet's position to sheet_name.

# Import pandas with the alias pd
import pandas as pd

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx", sheet_name=1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# Create a dataframe from the 2017 sheet by providing the sheet's name to read_excel().

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx", sheet_name='2017')

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()
