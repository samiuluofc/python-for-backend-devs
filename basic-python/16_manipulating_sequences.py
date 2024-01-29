"""
Manipulating sequence only possible for List (Mutable).
String and Tuple is not possible.
"""
from timeit import timeit

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# replace
l1[3] = 300
print(l1)

l1[1:3] = [20, 30, 40]
# different length, basically its replacing as well adding
print(l1)

l1[1:3] = [[20, 30, 40]]
print(l1)

l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2[::2] = [0, 20, 40, 60, 80, 100]  # even numbers
print(l2)
# But above placement needs LHS and RHS to represent same number of elements.
# Otherwise it will throw ValueError

# delete
del l1[1]
print(l1)

del l1[1:4]
print(l1)

del l1[::2]
print(l1)

del l1
# print(l1) will raise NameError as its not even exist anymore

# Append/Extend (more efficient than insert as doesn't need and shift)
l2.append(10000)
print(l2)
l2.extend([23, 34, 45])
print(l2)
l2.extend((1, 2, 3))
print(l2)
l2.extend('python')  # add each character as element
print(l2)
l2.extend(['python'])
print(l2)
l2.extend([(1, 3, 4)])
print(l2)
l2.extend([[23, 34, 45]])
print(l2)
del l2

# insert at index i
l3 = [10, 20, 30, 40, 50]
l3.insert(0, 'python')
print(l3)
l3.insert(3, 'python')
print(l3)

# Insert at the beginning is costly
l4 = [1]
print(timeit('l4.append(1)', globals=globals(), number=10000))
print(timeit('l4.insert(0, 1)', globals=globals(), number=10000))
