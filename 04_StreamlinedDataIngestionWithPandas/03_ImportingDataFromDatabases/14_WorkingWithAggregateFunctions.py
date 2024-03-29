# Working with aggregate functions

# Import pandas with the alias pd
import pandas as pd

# Create query to get temperature and precipitation by month
query = """
SELECT month,
        MAX(tmax),
        MIN(tmin),
        SUM(prcp)
  FROM weather
 GROUP BY month;
"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)
