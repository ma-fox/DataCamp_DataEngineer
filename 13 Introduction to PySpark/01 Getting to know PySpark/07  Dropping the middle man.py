# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv('/usr/local/share/datasets/airports.csv',
                          header=True)

# Show the data
airports.show()
