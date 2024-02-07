a = 50
b = 0
# res = a / b # Will raise ZeroDivisionError and terminates immediately

# Create an exception object (based on built-in exception class)
ex = KeyError("Hi this is Samiul. Its a value error.")
print(str(ex))  # display for user
print(repr(ex))  # display for programmer who knows python

# Start an exception flow
# raise ex # The display is called trace-back

# A program that raise an exception if you enter a name longer than 5 characters
name = str(input("Enter your name: "))
if len(name) > 5:
    raise ValueError(f'Name \'{name}\' is longer than 5 letters.')

# subclass test for python built-in exception
print(issubclass(KeyError, LookupError))
print(issubclass(ValueError, LookupError))
print(issubclass(IndexError, LookupError))
print(issubclass(LookupError, Exception))

# is 'ex' is an instance/object of the class ValueError (False)
print(isinstance(ex, ValueError))
# is 'ex' is an instance/object of the class KeyError (True)
print(isinstance(ex, KeyError))
print(isinstance(ex, LookupError))  # True

# True (so its also instance of the top level base class)
print(isinstance(ex, Exception))
