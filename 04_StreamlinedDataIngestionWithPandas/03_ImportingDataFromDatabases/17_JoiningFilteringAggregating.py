# Joining, filtering, and aggregating

# Import pandas with the alias pd
import pandas as pd

# Modify query to join tmax and tmin from weather by date
query = """
SELECT hpd311calls.created_date,
	   COUNT(*),
       weather.tmax,
       weather.tmin
  FROM hpd311calls
       JOIN weather
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER'
 GROUP BY hpd311calls.created_date;
 """

# Query database and save results as df
df = pd.read_sql(query, engine)

# View first 5 records
print(df.head())
