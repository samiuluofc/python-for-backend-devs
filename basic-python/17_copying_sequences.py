"""
Shallow copy vs Deep Copy

Shallow: create a new reference but still contains same objects as the other one.
That means, if it contains a mutable object and you modify it, it will impact the other.
Shallow copy only applies to List (mutable), not String and Tuple.

Deep: create a new reference, as well as copy the individual objects in it. So that means changing
one will NOT impact others. However, its costly, so use when absolutely needed
(when you know mutable objects in the list is going to change).
Deep copy is available for
"""
from copy import deepcopy

a = [1, 2, [3, 4]]
b = a  # Nor shallow nor Deep. Both has same reference
b.append(100)
print(a, b, a is b)

# Shallow copy
c = a.copy()  # or c = a[:], only available for list
c.append(200)
print(c, a, c is a)  # So no issue of adding a new object

# In the above list [3, 4] is an mutable object
c[2][0] = 'python'
print(c, a, c is a, c[2][0] is a[2][0])
# Damm! it modified on both, inner objects have same ref

# Lets do a deep copy
d = deepcopy(a)  # But its not necessary always.
d[2][0] = 'samiul'
print(d, a, d is a, d[2][0] is a[2][0])
# Now inner objects have different refs
