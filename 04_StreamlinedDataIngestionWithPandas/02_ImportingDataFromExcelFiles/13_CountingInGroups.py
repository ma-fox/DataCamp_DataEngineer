# Counting in groups

# Import pandas with the alias pd
import pandas as pd

# Create query to get call counts by complaint_type
query = """
SELECT complaint_type,
     COUNT(*)
  FROM hpd311calls
  GROUP BY complaint_type;
"""

# Create dataframe of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()
