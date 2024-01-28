"""
Immutable, homogenous sequence (sequence of unicode characters) type
"""

name = "Samiul Azam"  # Using literal
print(name)
name = str("Samiul Azam")  # Using constructor
print(name)

location = 'Calgary'  # can use single quotes as well
print(location)

location = '\'Calgary\''  # Using escape sequence to show quotes
print(location)

empty_str = ""
print(type(empty_str), empty_str)

empty_str = str()  # Constructor
print(type(empty_str), empty_str)

print(str(100))
print(str([1, 2, 3]))
print(str((1, 2, 3)))

# Accessing elements. Similar to list and tuples
print(location[1])
print(location[-2])
print(len(location))

# Immutability
# location[1] = 'C' # Its immutable like tuple

# Create a string with 10 0s.
msg = "0" * 10
print(msg)

# Convert a str to list/tuple
txt = 'python'
print(list(txt))
print(tuple(txt))

# Create a list of 0 to 9
list1 = list("0123456789")
print(list1)
