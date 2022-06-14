# Bringing it all together: Festivus!
import numpy as np

# Provided function in the DataCamp online environment
def welcome_guest(guest_and_time):
    """
    Returns a welcome string for the guest_and_time tuple.

    Args:
        guest_and_time (tuple): The guest and time tuple to create
            a welcome string for.

    Returns:
        welcome_string (str): A string welcoming the guest to Festivus.
        'Welcome to Festivus {guest}... You're {time} min late.'

    """
    guest = guest_and_time[0]
    arrival_time = guest_and_time[1]
    welcome_string = "Welcome to Festivus {}... You're {} min late.".format(
        guest, arrival_time)
    return welcome_string

# Provided list of names in the DataCamp online environment
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Create a list of arrival times
arrival_times = [*range(10, 60, 10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i], time) for i, time in enumerate(new_times)]

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')
