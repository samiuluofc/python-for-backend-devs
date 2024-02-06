"""
*   A collection of elements (hetroginous) without any ordering.
*   Each element in a set is unique.
*   It is an iterable. Unlike dictionary there is no order of insertion is maintained.
*   Like dictionary, set elements also need to hashable (immutable).
*   Type is set.
*   Sets are mutable (elements are immutable).
*   Frozenset is immutable and hashable.

"""

s = {1, 2, 2, 3, 4}
print(s, type(s), len(s))
s.clear()
s1 = s.copy()  # same way it does the shallow copy

s = set([1, 2, 2, 3, 4])
print(s, type(s), len(s))

s = set(
)  # empty set. We cannot have {} as empty set as its an empty dict actually.
print(s, type(s), len(s))

s = set('Samiul Azam')
print(s, type(s), len(s))

# membership test
print('u' in s)
print('k' in s)

# looping
for element in s:
    print(element)
