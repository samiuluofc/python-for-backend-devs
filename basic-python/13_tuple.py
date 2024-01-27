"""
Similar to List, BUT its immutable container type.
That means once a tuple has been created, you are not allowed to add/remove/replace any elements.
However, we can modify the objects inside the tuple. So basically the collection is immutable.

When to use tuple over list:
    Tuples use less memory than lists. They are also a bit faster,
    especially when you're just looking up values. So, if you have
    data that you don't want to change, it's better to use tuples
    instead of lists.
"""

t0 = (
)  # Empty tuple, but its useless, cause we cannot add any element into it
print(type(t0), t0)
t1 = (5, )  # Tuple with 1 element
print(type(t1), t1)

t2 = (10, 20, 30, 40)  # Tuple created using literal
t3 = 1, 2, 3, 4, 5  # # Tuple created using literal. () is not mandatory, but good practice to have it
print(type(t2), t2)
print(type(t3), t3)
t4 = tuple([1, 2, 3, 4, 5])  # list created using tuple constructor function
print(type(t4), t4)

# list can be heterogenous, can contains any other objects, tuple itself
t5 = (1, 2, 3, [True, False], (4, 5))
print(t5)

# Accessing tuple elements (same as list)
print(t1[0])
ind = 0
print(t1[ind])
print(t5[3])
print(t5[3][1])
print(len(t5))  # built-in len() function. Result is 5.
print(len(t5[3]))  # built-in len() function. Result is 2.
# print(t1[100]) # Will cause IndexError
print(t3[-1])  # access the last element using negative index
print(t3[-2])  # access the second last element using negative index

# Replace/add/remove of an element in a tuple is not allowed:
# t1[0] = 1000 # Returns TypeError

# However, you can modify the individual objects
# In t5, t5[3] is a list [True, False] which is mutable. So we can modify it, but cannot replace it whole.
t5[3][1] = True
# t3[3] = [True, True] # Not allowed
print(t5)
