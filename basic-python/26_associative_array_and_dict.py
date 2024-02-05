"""
Dictionary is most important data structure in python.

in python association is every where:
    * variable name is associated (pointing) to an object in memory.
    * objects are also dictionary:
        * properties are symbol/variables associated to some value (ob.variable)
        * methods are names associated to some function (ob.method())
Associating two things together is extremely useful and its every where in python/real-life.
* name to phone number
* dns to IP address

Associative array means:
* You have a key array which contains all the keys.
* You have a value array which contains the value of the corresponding key in the same index.
* Basically you need to search (get the index) the key in the key array. Use that index to
retrieve the value from the value array.

Basically we need to lookup a list of key:value pairs (map between key and value).

Formally its called associative arrays or maps:
* its an abstract concept, can be implemented in different ways
* Dictionaries (hash maps) are one of the concrete implementation.


With dictionary, lookup speed does not affected by the dictionary size (order 1).
Features of Dictionary:
* key must be something that is hashable: strings, float, int, tuple, bool
* key must be unique
* key must be immutable object
* value can be any object/any type
* Dictionary type is 'dict'
* Dictionary is a collection of key:value pair
* Dictionary is an iterable, but it is not a sequence (like Set).
* Dictionary is mutable
"""

d = {}  # An empty dictionary
print(d, type(d), len(d))
d = {'a': 1, 'b': 2, 'c': 3}
print(d, type(d), len(d))

person = {'first_name': 'Samiul', 'last_name': 'Azam', 'year_born': 1988}
print(person)
print(person['year_born'])
person['month_born'] = 'December'
print(person)
del person['month_born']
print(person)

# Anything that is immutable has unique hash code. That is why any immutable can be used as key in dictionary.
print(hash(100))
print(hash(3.14))
print(hash('samiul'))
print(hash((1, 2, 3)))
#print(hash([1,2,3,4])) # Type error
#print(hash((1,2,[3,4]))) # Type error cause not every object in the tuple is hashable

# Note: accessing non-existing key will return 'keyError'

# Interesting!!!
current_scope = globals()
print(type(current_scope), len(current_scope))
print(current_scope['__doc__'])
