"""

Set operations:
    * Disjoint
    * Subset, superset, strict subset, strict superset
    * Union, intersection, difference
    * Add, remove, discard
    * Membership test

REMEMBER:
* membership test using 'in' for set is much faster than list and tuple
* Set is a nice tool to find/gather common elements from multiple list/tuple/set
# Nice tool to use for eliminating duplicates
"""

import string  # A collection of string constant (ascii only)

# Disjoint: two sets are disjoint when there is no element in common
s1 = {1, 2, 3, 4, 5}
s2 = {'a', 'b', 'c', 'd'}
s3 = {5, 6, 7, 8, 9}
s4 = set('abcdef')

print(s4)
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))
print(s1.isdisjoint(s3))  # 5 is common element
print(s1 == s1)
print(s2 != s3)

# add, remove, discard
s5 = set()  # empty set
s5.add(1)
s5.add(2)
s5.add(3)
s5.add(4)

s5.remove(1)
# s5.remove(10) # Will raise KeyError if non-exist
s5.discard(2)
s5.discard(10)  # Will do nothing if non-exist
print(s5)

s5.clear()
print(len(s5))

# subset n superset
s1 = set('abc')
s2 = set('abcdef')
s3 = set('cba')
s4 = set('defghi')

print(s1 < s2)  # s1 is strict subset of s2
print(s2 > s1)  # s2 is strict superset of s1
print(s1 < s3)  # s1 is not strict subset of s3
print(s1 > s3)  # s1 is not strict superset of s3
print(s1 <= s3)  # s1 is subset of s3
print(s3 >= s1)  # s1 is superset of s3

# Union, intersection and difference

print(s2 | s4)  # union
print(s2 & s4)  # intersection
print(s2 - s4)  # difference
print(s4 - s2)

print(s1.union(s2))
print(s1)  # No mutation

# Note: WE can convert a set to list/tuple using list() and tuple() constructor
print(list(s1))
print(tuple(s1))

# Create a set of all alpha numeric letters
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
s = set(string.ascii_lowercase) | set(string.digits) | set(
    string.ascii_uppercase)  # Union
print(s, type(s), len(s))
