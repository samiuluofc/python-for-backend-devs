"""
Special methods starts with double underscore and ends with double underscore.
Referred as 'dunder' method.

Some of the popular ones:
* __str__ # string representation of an object when print or str function is used on a object (simple and useful for users)
* __repr__ # Same as __str__ but this is used for developers.
* __eq__ # equal '==' or not (default: whether they are same object of not). p1 == p2 means p1.__eq__(p2.)
* __lt__ # operator overloading
* __add__ # operator overloading

print() uses __str__ first if its available, then __repr__.
Otherwise the default "class name and object id"



"""


class Circle:
    _PI = 3.1416

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return self._PI * (self.radius**2)

    def __str__(self):
        return f"Circle with a radius ({self.radius})"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            False

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            False


c = Circle(10)
d = Circle(10)
e = Circle(20)
print(c)  # Default behavior: Class name and object id
print(str(c))
print(repr(c))  # Default behavior: Class name and object id
print(
    c == d)  # Default: c is d (are they same object? not comparing the value)
print(d < e)
print(c < d)
