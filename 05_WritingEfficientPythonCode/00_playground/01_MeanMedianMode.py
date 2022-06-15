# This is a list of numbers that we will use to calculate the mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

print(f"The list is: \n{list1}\n")

# Mean
# The Mean is the average value of all the values in a dataset.
# In other words, the Median is the middle value in a dataset.
# It is also called the average of the dataset, 'typical' or 'middle', or the 'Central Tendency'.
# To calculate the Mean value of a dataset,
# we first need to find the sum of all the values and then divide the sum of all the values by the total number of values

# This variable will hold the sum() of all the numbers in the list and divide it by the number of numbers in the list using the len() function
mean = sum(list1) / len(list1)

print(f"The MEAN value of the list is: {mean}\n")

# Median
# The Median is the middle value among all the values in sorted order.
# Here we need to calculate the mid-value of all the values in a dataset.
# But before calculating the Median, we need to arrange all the values in sorted order.
# There are two different ways of calculating the median value:

# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}thterm

# list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:
    m1 = list1[len(list1) // 2]
    m2 = list1[len(list1) // 2 - 1]
    median = (m1 + m2) / 2
else:
    median = list1[len(list1) // 2]
print(f"The MEDIAN value of the list is: {median}\n")

# Mode
# Mode is the most frequently occurring value(s) among all the values.
# Below is how we can calculate the mode value of a dataset using Python:

# list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(f"The MODE value of the list is: {mode}")
print(f"Note that this implementation works ONLY for single value\n")

# Easy version:
# The mode() function in the python statistics module takes some dataset as a parameter and returns its mode value.

from statistics import mode

A = [10, 20, 20, 30, 30 ,30]
print("Mode of List A using 'mode' is % s" % (mode(A)))
B = ['Yes', 'Yes', 'Yes', 'No', 'No']
print("Mode of List B using 'mode' is % s\n" % (mode(B)))

from statistics import multimode

C = [10, 20, 20, 20, 30, 30, 30]
print("Mode of List C using 'multimode' is % s" % (multimode(C)))
D = ['Yes', 'Yes', 'Yes', 'No', 'No', 'No']
print("Mode of List D using 'multimode' is % s\n" % (multimode(D)))
