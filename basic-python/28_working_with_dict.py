from copy import deepcopy

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# Search a key (membership test) in Dict (order 1, very fast)
# membership test in dict is very fast, way faster than list.

print('four' in d)  # True
print('four' in d.keys())  # True
print('seven' in d)  # False
print('seven' not in d)  # True
print(4 in d.values())  # True

print(len(d))  # 5
# d.clear() # make it empty

# Copies (Shallow vs deep)
# Deep copy takes much longer time than shallow
d1 = d.copy()  # shallow
print(id(d1), id(d))  # Have two different refs

# Note: if a dictionary has all immutable objects (keys and values),
# there is no point of doing deepcopy, cause keys or values will never change.
# Keys are always immutable. Values can be mutable such as another dict or list.abs
# In that case deepcopy make sense.
d3 = {'list1': [1, 2, 3, 4], 'list2': {'one': 1, 'two': 2}}

d2 = d3.copy()
print(id(d3), id(d2))  # Different
print(id(d3['list1']), id(d2['list1']))  # inner object has same ref

# Now deepcopy make sense
d4 = deepcopy(d3)
print(id(d3), id(d4))  # Different
print(id(d3['list1']), id(d4['list1']))  # inner object has different ref

# Creating dictionary with dict constructor/function
d5 = dict(
    one=1, two=2,
    three=3)  # limitation: keyword argument must be a valid variable name.
print(d5)

d5 = dict.fromkeys(['one', 'two', 'three'], 0)  # initialized all with zero
print(d5)

d5 = dict.fromkeys('python', 1)  # initialized all with one
print(d5)

d5 = dict.fromkeys(['a', 'a', 'b', 'b'], 10)
print(d5)  # Ignores the repeated keys
print(list(d5))

# Frequency count of letters
msg = 'Python is an awesome programming language'
d = dict.fromkeys(msg, 0)
print(d)

for ch in msg:
    d[ch] += 1
print(d)

# Get method
d = {'a': "sami", 'b': "emon", 'c': "nobin"}
print(d.get('a', 'no_name'))  # if not as a key, then return no_name
print(d.get('d', 'no_name'))

# Merge dictionary
d1 = {'a': "sami", 'b': "emon", 'c': "nobin"}
d2 = {'c': "sajib", 'b': 2, 'd': "anik"}
d1.update(d2)
print(d1)  # d1 is mutated, but d2 remains same

d1 = {'a': "sami", 'b': "emon", 'c': "nobin"}
d2 = {'c': "sajib", 'b': 2, 'd': "anik"}
d2.update(d1)
print(d2)  # d2 is mutated, but d1 remains same.
