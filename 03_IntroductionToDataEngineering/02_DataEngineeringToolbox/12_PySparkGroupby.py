# The methods you're going to use in this exercise are:

# .printSchema(): helps print the schema of a Spark DataFrame.
# .groupBy(): grouping statement for an aggregation.
# .mean(): take the mean over each group.
# .show(): show the results.

# Print the type of athlete_events_spark
print(type(athlete_events_spark))

# Print the schema of athlete_events_spark
print(athlete_events_spark.printSchema())

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age'))

# Group by the Year, and find the mean Age
print(athlete_events_spark.groupBy('Year').mean('Age').show())
