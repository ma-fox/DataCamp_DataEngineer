# Counter
# You're working on a new web app, and you are curious about how many times each of the functions in it gets called. So you decide to write a decorator that adds a counter to each function that you decorate. You could use this information in the future to determine whether there are sections of code that you could remove because they are no longer being used by the app.

# Call the function being decorated and return the result.
# Return the new decorated function.
# Decorate foo() with the counter() decorator.


def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func(*args, **kwargs)

  #initialise counter
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')

foo()
foo()

print('foo() was called {} times.'.format(foo.count))


# <script.py> output:
#     calling foo()
#     calling foo()
#     foo() was called 2 times.



# Cool counting! Now you can go decorate a bunch of functions with the counter() decorator, let your program run for a while, and then print out how many times each function was called.

# It seems a little magical that you can reference the wrapper() function from inside the definition of wrapper() as we do here on line 3.
# That's just one of the many neat things about functions in Python -- any function, not just decorators.
