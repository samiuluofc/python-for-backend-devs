"""
Unary operator (operates on one operand)
Binary operator (operates on two operands).
Ternary operator (operates on two operands).

Arithmetic operator operates on int and float numbers.
"""

print(-10)  # Unary operator
print(
    20 - 10.0
)  # Binary operator, returns float type as one of the operand is float, so the
print(4 / 2)  # returns float type
print(3 / 2)  # returns float type
print(3 * 2)  # returns int type
print(3 * 2.1)  # returns float type
print(2**4)  # returns int type, its x to the power y
print(2**-4)  # returns float type
print(2**-2.2)  # returns float type
print(16**(1 / 2))  # This is actually sqrt
print(20 // 3)  # integer division
print(20 / 3)  # float division
print(20 % 3)  # integer mod
c = (-4)**0.5  # returns complex number
print(type(c))
print(c.imag, c.real)
# operator may returns different types of data depending on operand's type
"""
In python numbers are objects. Depending on the operator,
it actually calls a member function with second operand as function parameter
"""
num_1 = 10
num_2 = 20
print(num_1.__add__(num_2))
print(num_2.__sub__(num_1))
print(num_1.__mul__(num_2))


# Lets create a a custom data-type/class called Vector to show how operator overloading works in python.
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


v1 = Vector(1, 1)
v2 = Vector(2, 2)
print(v1, v2)
v3 = v1 + v2
print(v3)
print(type(v3))
