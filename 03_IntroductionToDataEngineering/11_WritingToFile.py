## Writing to a file
# Apache Parquet is a popular column storage file format used by Hadoop systems, such Spark.
# Parquet files are a binary format that can be read and written by many different systems.

# Write the pandas DataFrame to parquet
film_pdf.to_parquet('films_pdf.parquet')

# Write the PySpark DataFrame to parquet
film_sdf.write.parquet('films_sdf.parquet')
