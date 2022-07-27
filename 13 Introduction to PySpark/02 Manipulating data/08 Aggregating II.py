# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(
    flights.origin == "SEA").groupBy().avg("air_time").show()


# +------------------+
# |     avg(air_time)|
# +------------------+
# |188.20689655172413|
# +------------------+


# Total hours in the air
flights.withColumn("duration_hrs",
                   flights.air_time / 60).groupBy().sum("duration_hrs").show()

# +------------------+
# | sum(duration_hrs)|
# +------------------+
# |25289.600000000126|

# flights.show()
# |year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|tailnum|flight|origin|dest|air_time|distance|hour|minute|
