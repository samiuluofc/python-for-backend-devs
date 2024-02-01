"""
Python has a ton of string methods:
https://docs.python.org/3/library/stdtypes.html#string-methods

my_str.method() dot notation is used to access an object attributes.
String is immutable. So these methods always return a new string.
"""
from timeit import timeit

# Case modification
message = "Calgary is an Awesome city to live."
print(message.upper())
print(message.lower())
print(message.title())
print(message.swapcase())
print('abC'.lower() == 'AbC'.lower())  # Safer way to do string comparison

# Unicode issue
msg = '\N{LATIN SMALL LETTER SHARP S}'.lower()
msg_upper = msg.upper()
print(msg, msg_upper)  # Even the length is different
print(msg.lower() == msg_upper.lower())  # False, which is wrong
print(msg.casefold() ==
      msg_upper.casefold())  # always use this to handle any unicode character

# Striping
msg = "  --Samiul Azam--  "
print(msg.strip())
print(msg.rstrip())
print(msg.lstrip())
print(msg.strip('- '))  # strip - and space

# concate
msg = "samiul" + " " + "azam"
print(msg)

# join and split
msg = 'Calgary-is-an-Awesome-city-to-live'
word_list = msg.split('-')
print(word_list)
print('-'.join(word_list))
print('-'.join('samiulazam'))  # string itself is a sequence

# substring
print('City' in message)  # case sensitive
print('CITY'.lower() in message.lower())  # casefold is much better
print('m' in "samiul")
print(3 in [1, 2, 3, 4, 5])
print('abc' in ['sam', 'emon', 'abc'])
print(msg.startswith('Calgary'))
print(msg.endswith('Live'))
print(msg.lower().endswith('Live'.lower()))
print(msg.index('live'))  # return the position
print([1, 2, 3, 4,
       5].index(3))  # works for other sequences tuple and list as well

# Note 'in' is faster than find and index.
t = timeit("'live' in msg", globals=globals(), number=1_000_000)
print(t)
t = timeit("msg.find('live')", globals=globals(), number=1_000_000)
print(t)
t = timeit("msg.find('live')", globals=globals(), number=1_000_000)
print(t)
