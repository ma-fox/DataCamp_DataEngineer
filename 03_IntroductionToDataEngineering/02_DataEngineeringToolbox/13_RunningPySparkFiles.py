from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    athlete_events_spark = (spark
        .read
        .csv("/home/repl/datasets/athlete_events.csv",
             header=True,
             inferSchema=True,
             escape='"'))

    athlete_events_spark = (athlete_events_spark
        .withColumn("Height",
                    athlete_events_spark.Height.cast("integer")))

    print(athlete_events_spark
        .groupBy('Year')
        .mean('Height')
        .orderBy('Year')
        .show())

# You can use spark-submit as follows:

# spark-submit \
#   --master local[4] \
#   /home/repl/spark-script.py

# What does this output?
# A DataFrame with average Olympian heights by year!
