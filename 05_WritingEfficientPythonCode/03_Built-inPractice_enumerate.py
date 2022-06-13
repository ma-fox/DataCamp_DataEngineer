# Built-in practice: enumerate()

# Rewrite the for loop to use enumerate

indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)

# Using Python's built-in enumerate() function allows you to create an index for each item in the object you give it.
# You can use list comprehension, or even unpack the enumerate object directly into a list, to write a nice simple one-liner.
