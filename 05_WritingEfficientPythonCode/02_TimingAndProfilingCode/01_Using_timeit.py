# Using %timeit: your turn!

import numpy as np
# testing using timeit(), which is only available in Python 3 using jupyter notebook!

# Use list comprehension and range() to create a list of integers from 0 to 50 called nums_list_comp.

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Use range() to create a list of integers from 0 to 50 and unpack its contents into a list called nums_unpack.
# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)

# Create a list of integers (0-50) using list comprehension
%timeit nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
%timeit nums_unpack = [*range(51)]
print(nums_unpack)

# Fazit:
# Unpacking the range object was faster than list comprehension.
