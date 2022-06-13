# Built-in practice: map()

# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*list(names_map)]

# Print the list created above
print(names_uppercase)

# You used Python's built-in map() function to apply the str.upper() method to each element in the names object.
# Later on in the course, you'll explore how using map() can provide some efficiency improvements to your code.
