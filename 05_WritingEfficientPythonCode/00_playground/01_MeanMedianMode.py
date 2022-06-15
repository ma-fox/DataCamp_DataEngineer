# This is a list of numbers that we will use to calculate the mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

# Mean
# The mean is the average value of all the values in a dataset.
# To calculate the mean value of a dataset,
# we first need to find the sum of all the values and then divide the sum of all the values by the total number of values

# This variable will hold the sum() of all the numbers in the list and divide it by the number of numbers in the list using the len() function
mean = sum(list1) / len(list1)

print(mean)

# Median
# The Median is the middle value among all the values in sorted order. Here we need to calculate the mid-value of all the values in a dataset. But before calculating the Median, we need to arrange all the values in sorted order. There are two different ways of calculating the median value:

# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}thterm
