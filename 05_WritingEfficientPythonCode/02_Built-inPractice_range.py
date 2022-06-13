# Built-in practice: range()

# In this exercise, you will practice using Python's built-in function range(). Remember that you can use range() in a few different ways:

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1, 12, 2)]
print(nums_list2)

# Notice that using Python's range() function allows you to create a range object of numbers without explicitly typing them out.
# You can convert the range object into a list by using the list() function or by unpacking it into a list using the star character (*).
