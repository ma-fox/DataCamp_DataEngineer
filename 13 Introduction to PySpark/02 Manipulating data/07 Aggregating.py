# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

# +-------------+
# |min(distance)|
# +-------------+
# |          106|
# +-------------+



# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()

# +-------------+
# |max(air_time)|
# +-------------+
# |          409|
# +-------------+

# flights.show()
# |year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|tailnum|flight|origin|dest|air_time|distance|hour|minute|
