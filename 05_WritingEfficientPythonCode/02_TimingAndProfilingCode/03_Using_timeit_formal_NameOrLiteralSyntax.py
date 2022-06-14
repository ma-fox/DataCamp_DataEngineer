# Using %timeit: formal name or literal syntax

# data structure	formal name	    literal syntax
# list	            list()	        []
# dictionary	    dict()	        {}
# tuple	            tuple()	        ()

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

# Use %timeit in your IPython console to compare runtimes between creating a list using the formal name (list()) and the literal syntax ([]).
# Don't use print() when timing your code, because %timeit will print out the results without the print() statements.

%timeit formal_list = list()
# 74 ns +- 2.74 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

%timeit literal_list = []
# 23.4 ns +- 1.77 ns per loop (mean +- std. dev. of 7 runs, 10000000 loops each)

# The comparison shows that the formal name is faster than the literal syntax.
# Therefore it is preferable to use the formal name when creating a list.
# So, consider using the literal syntaxes,
# (like [] instead of list(), {} instead of dict(), or () instead of tuple()), where applicable, to gain some speed.
