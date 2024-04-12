"""
We set/get any attribute of an object 'directly' using dot notation. There is no restriction.
* No control over what assigned values are during 'setting' a value
* No control over formatting or modifying attribute values during 'getting' the value


Use special @property decorator and have the setter and getter function in place.

class Person():
    def __init__(self, name):
        self._name = name # using '_' means its acting as a private variable (convention)

    @property
    def name(): # getter
        return self._name

    @name.setter # setter for name
    def name(self, value):
        self._name = value

Note: Both getter and setter must use the same name
Note: If there is no setter, the attribute will be read only
"""
from typing import Union


class Circle():
    _PI = 3.1416

    def __init__(self, radius: Union[int, float]):
        self.radius = radius  # calling the setter using self.radius
        # Taking the benefit of setter at init time

    @property
    def area(self):
        return self._PI * (self.radius**2)

    # However, after initialization of the object
    # anyone can put string value for self._radius (ob._radius = 'hello')
    # To prevent that we can have setter and getter for 'radius' attribute.abs
    @property
    def radius(self):
        return self._radius  # Dont use self.radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius can not be less than zero")
        # '_' just a convention to indicate it as private (internal to the class)
        self._radius = value

    # Note: if there is no setter, no one can do ob.radius = value.
    # Making it read only attribute.


c = Circle(10)

print(c.radius)  # Calling the 'radius' method, but no need to use braces.and
print(c.area)  # No braces needed to call, cause its a property as well
c.radius = 20  # Calling the setter function
print(c.area)
