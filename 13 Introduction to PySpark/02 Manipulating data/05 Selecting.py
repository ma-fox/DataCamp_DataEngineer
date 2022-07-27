# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

# Define first filter
filterA = flights.origin == "SEA"

# Define second filter
filterB = flights.dest == "PDX"

# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)

selected1.show()
# +-------+------+----+
# |tailnum|origin|dest|
# +-------+------+----+
# | N846VA|   SEA| LAX|
# | N559AS|   SEA| HNL|
# | N847VA|   SEA| SFO|
# | N360SW|   PDX| SJC|
# | N612AS|   SEA| BUR|
# | N646SW|   PDX| DEN|
# | N422WN|   PDX| OAK|
# | N361VA|   SEA| SFO|
# | N309AS|   SEA| SAN|
# | N564AS|   SEA| ORD|
# | N323AS|   SEA| LAX|
# | N305AS|   SEA| PHX|
# | N433AS|   SEA| LAS|
# | N765AS|   SEA| ANC|
# | N713AS|   SEA| SFO|
# | N27205|   PDX| SFO|
# | N626AS|   SEA| SMF|
# | N8634A|   SEA| MDW|
# | N597AS|   SEA| BOS|
# | N215AG|   PDX| BUR|
# +-------+------+----+
# only showing top 20 rows

selected2.show()
# +------+----+-------+
# |origin|dest|carrier|
# +------+----+-------+
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     AS|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     AS|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# |   SEA| PDX|     OO|
# +------+----+-------+
# only showing top 20 rows
