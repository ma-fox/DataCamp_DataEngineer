# Define avg_speed
avg_speed = (flights.distance / (flights.air_time / 60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum",
                            "distance/(air_time/60) as avg_speed")

speed1.show()
# +------+----+-------+------------------+
# |origin|dest|tailnum|         avg_speed|
# +------+----+-------+------------------+
# |   SEA| LAX| N846VA| 433.6363636363636|
# |   SEA| HNL| N559AS| 446.1666666666667|
# |   SEA| SFO| N847VA|367.02702702702703|
# |   PDX| SJC| N360SW| 411.3253012048193|
# |   SEA| BUR| N612AS| 442.6771653543307|
# |   PDX| DEN| N646SW|491.40495867768595|
# |   PDX| OAK| N422WN|             362.0|
# |   SEA| SFO| N361VA| 415.7142857142857|
# |   SEA| SAN| N309AS| 466.6666666666667|
# |   SEA| ORD| N564AS| 521.5151515151515|
# |   SEA| LAX| N323AS| 440.3076923076923|
# |   SEA| PHX| N305AS|431.29870129870125|
# |   SEA| LAS| N433AS| 409.6062992125984|
# |   SEA| ANC| N765AS|474.75409836065575|
# |   SEA| SFO| N713AS| 315.8139534883721|
# |   PDX| SFO| N27205| 366.6666666666667|
# |   SEA| SMF| N626AS|477.63157894736844|
# |   SEA| MDW| N8634A|481.38888888888886|
# |   SEA| BOS| N597AS| 516.4137931034483|
# |   PDX| BUR| N215AG| 441.6216216216216|
# +------+----+-------+------------------+
# only showing top 20 rows


speed2.show()
# +------+----+-------+------------------+
# |origin|dest|tailnum|         avg_speed|
# +------+----+-------+------------------+
# |   SEA| LAX| N846VA| 433.6363636363636|
# |   SEA| HNL| N559AS| 446.1666666666667|
# |   SEA| SFO| N847VA|367.02702702702703|
# |   PDX| SJC| N360SW| 411.3253012048193|
# |   SEA| BUR| N612AS| 442.6771653543307|
# |   PDX| DEN| N646SW|491.40495867768595|
# |   PDX| OAK| N422WN|             362.0|
# |   SEA| SFO| N361VA| 415.7142857142857|
# |   SEA| SAN| N309AS| 466.6666666666667|
# |   SEA| ORD| N564AS| 521.5151515151515|
# |   SEA| LAX| N323AS| 440.3076923076923|
# |   SEA| PHX| N305AS|431.29870129870125|
# |   SEA| LAS| N433AS| 409.6062992125984|
# |   SEA| ANC| N765AS|474.75409836065575|
# |   SEA| SFO| N713AS| 315.8139534883721|
# |   PDX| SFO| N27205| 366.6666666666667|
# |   SEA| SMF| N626AS|477.63157894736844|
# |   SEA| MDW| N8634A|481.38888888888886|
# |   SEA| BOS| N597AS| 516.4137931034483|
# |   PDX| BUR| N215AG| 441.6216216216216|
# +------+----+-------+------------------+
# only showing top 20 rows
