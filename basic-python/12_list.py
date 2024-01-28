"""
List is a container type sequence.
List is builtin mutable sequence.
Elements are indexed, starts from 0.
List is mutable, we can add, remove, replace elements of a list.
List is heterogenous, that means we can have different types of objects in a list.
List has unbounded growth, but it still finite.

Lists are objects:
    State: elements in the list
    Functionality: add, remove, replace, retrieve elements
"""

list1 = [10, 20, 30, 40]  # list created using literal
print(list1)
print(type(list1))
list2 = list([1, 2, 3])  # list created using list constructor function
print(list2)
list3 = [1, 2, 3,
         [True, False]]  # list can be heterogenous, can contains another list
print(list3)

# Accessing list elements
print(list1[1])
ind = 3
print(list1[ind])
print(list3[3][1])
print(len(list3))  # built-in len() function. Result is 4.
print(len(list3[3]))  # built-in len() function. Result is 2.
# print(list1[100]) # Will cause IndexError
print(list1[-1])  # access the last element using negative index
print(list1[-2])  # access the second last element using negative index

# Replace list element:
list1[0] = 1000
print(list1)
list3[3][0] = False
print(list3)

# Creating empty list
a = []
print(len(a))
b = list()
print(len(b))

# Create a list with 10s of 0s.
a = [0] * 10
print(a)
