class Person:
    """A class for a Person. Basically it will contain
    all the attributes (states) and methods for a person"""

    def __init__(self, age=100, first_name='No name', last_name='No name'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        print(self)


p1 = Person(100, 'Enamul', 'Karim')
print(
    p1
)  # Same as the print(self). That means self contains the ref to the object
# print(help(Person))
print(p1.__class__)
print(p1.__doc__)
print(p1.__dict__)  # attributes are stored as dict
print(Person.__name__)
dir(p1)
print(type(p1) is Person)
print(isinstance(p1, Person))

p1.address = "Calgary"  # for custom object its possible, but not a good practice
print(p1.__dict__)
del p1.address  # for custom object its possible, but not a good practice
print(p1.__dict__)


class Point:

    def __init__(self, *coords):  # same as *args
        self.coordinates = coords


p = Point(1, 2, 3, 4)
print(p.__dict__)


class Circle:

    def __init__(self, *, radius=1):  # no positional arguments allowed
        if radius < 0:
            raise ValueError("Radius must be a positive number")
        self.radius = radius


c = Circle(radius=10)
print(c.__dict__)
vars(c)  # same as print(c.__dict__)
