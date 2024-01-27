"""
Relational operators: >, >=, <, <=, ==, !=
Facts:
*   Dont use == with floats number. Cause 0.1 + 0.1 + 0.1 == 0.3 is False, because the finite representation of a float number.
*   Hello > 10 will raise TypeError, however hello == 10 will return false. However, never compare string with a number.
*   Remember relational operator == is actually comparing the values of two objects not the object as a whole.
*   Remember everything in python is an object.
*   'is' (identity comparison operator) is used to find whether two objects are same or not. Is uses memory address to determine it.
*   'in' and 'not in' are membership operators.
*   The type of object will define what the results will be for Relational operations. Cause object's member functions
such as __lt__, __gt__, __eg__ has the logic for <, > and ==.
"""

# print('hello' > 10) # Will raise TypeError
print('hello' == 10)  # False
print(1 == 1.0)  # True
print(1 is 1.0)  # False

a = 100  # remember integer objects are immutable
b = 100
print(a is b)  # True. Its actually same as id(a) == id(b)
print(id(a))  # gives you memory address
print(id(b))  # basically 'is' means id(a) == id(b)
print(a.__eq__(b))

s = {1, 2, '3', 'hello', 12.86}  # its a Set (a collection)
print(3 in s)  # False
print('hello' in s)  # True
print('test' not in s)  # True
print(12.86 not in s)  # False

d = 10_000_000  # Another way to right integer, easy to read when there is a _ after every 3 digits
print(d, type(d), id(d))

# complex numbers: It does not support <, <=, >, >=, but it supports == and !=
a = 1 + 1j
print(a, type(a))


# Custom class/object
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(
        self
    ):  # this function should define what to display when we print the object
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):  # + operator overloading
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.x + other.x
            return Vector(x, y)

    def __eq__(
        self, other
    ):  # By default its based on id/memory address, but we override it here to do the right thing
        if isinstance(other, Vector):
            if (other.x == self.x and other.y == self.y):
                return True
        return False


v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(2, 3)
print(v1 == v2)  # True
print(v1 == v3)  # False
print(
    v1 is v2
)  # False, they created on a different memory address as they are two different objects
print(id(v1), id(v2))
