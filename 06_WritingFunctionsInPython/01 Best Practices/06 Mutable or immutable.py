Mutable or immutable?
The following function adds a mapping between a string and the lowercase version of that string to a dictionary. What do you expect the values of d and s to be after the function is called?

def store_lower(_dict, _string):
  """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`

  Args:
    _dict (dict): The dictionary to update.
    _string (str): The string to add.
  """
  orig_string = _string
  _string = _string.lower()
  _dict[orig_string] = _string

d = {}
s = 'Hello'

store_lower(d, s)




d = {}, s = 'Hello'
d = {}, s = 'hello'
d = {'Hello': 'hello'}, s = 'hello'
d = {'hello': 'hello'}, s = 'hello'

#YES - d = {'Hello': 'hello'}, s = 'Hello'
When the function assigns _string.lowercase() back to the _string variable, it disconnects _string from both s and orig_string.
Correct! Dictionaries are mutable objects in Python, so the function can directly change it in the _dict[_orig_string] = _string statement.
Strings, on the other hand, are immutable. When the function creates the lowercase version, it has to assign it to the _string variable.
This disconnects what happens to _string from the external s variable.
