"""
Iterable is a collection of objects that can be iterated over.
    * Sequences are iterable (positional order)
    * Dictionaries are iterable (insertion order)
    * Sets are iterable (no guaranteed order)

Iterator is some code that is able to give us next element when we request it.
    * It can use a collection to pick the next element from the collection OR
    * It can be a function which generates the next element for you

So iterable and iterator are two different things.
"""
"""
An iterable is a collection that can be iterated over.
But still, we need something that can:
*   Give us the next item
*   Keep track of what's so far given to us
*   Inform us there is nothing left to give us
*   This is called iterator.

Iterable does  ot know anything about how its going to iterate.
However, it knows how to create and give us an iterator when we need it.
Iterables implement a special method called __iter__() that returns a new iterator.
Can also be called by iter() function.

Iterator has a special method called __next__(). We can use next() function as well.
Iterator is one time use, we cannot reuse it once it serves all objects in an iterables.
Iterator raises StopIteration, when there is nothing left in the iterable.

The key thing here is that, iterator has some state. But there is no going back
or starting from the beginning again.

Iterators are one time use only. If you want to go back, you need to create a new iterator.

"""

l = [1, 2, 3, 4, 5]
iterator = iter(l)  # give me an iterator for l

print(type(iterator))

# Now we can use this iterator to iterate through l
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # Raise StopIteration exception

# Iterator remembers the which element has been given already
# No way to go back. No way to reuse an iterator. We need to create a new one if needed.

# Internally for loop is using similar approach. We can mimic the same behavior

print(id(iterator))
iterator = iter(l)  # gives a new iterator object always
print(id(iterator))  # Pointing to different object

try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    pass

# Note: range object is not an iterator, its an iterable (Generator), but not a collection.
# Its generates number one by one on demand (lazy). Memory efficient and faster.

r = range(1, 7)
iterator = iter(r)
print(type(iterator))

try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    pass

# enumerate is an iterator, not iterable
enum = enumerate(l)
print(type(enum))
print(next(enum))
print(next(enum))
print(list(enum))  # all remaining become a list
print(list(enum))  # Nothing available to iter

# object that supports both iter and next functions are iterators.
# object that supports only iter is iterable. Next is not allowed on iterables.

# Most often python returns iterators instead of iterable, cause its memory efficient and faster.
