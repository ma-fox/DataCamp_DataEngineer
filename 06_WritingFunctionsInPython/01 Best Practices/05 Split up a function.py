Split up a function
Another engineer on your team has written this function to calculate the mean and median of a list. You want to show them how to split it into two simpler functions: mean() and median()
def mean_and_median(values):
  """Get the mean and median of a list of `values`

  Args:
    values (iterable of float): A list of numbers

  Returns:
    tuple (float, float): The mean and median
  """
  mean = sum(values) / len(values)
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]

  return mean, median








Write the mean() function.
def mean(values):
  """Get the mean of a list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the mean() function
  mean = sum(values) / len(values)
  return mean










Write the median() function.
def median(values):
  """Get the median of a list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the median() function
  midpoint = int(len(values) / 2)

  # Note that the int midpoint above starts from 1
  # Note that the position within the lists below start from 0
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]
  return median


A perfect split! Each function does one thing and does it well. Using, testing, and maintaining these will be a breeze (although you'll probably just use numpy.mean() and numpy.median() for this in real life).
