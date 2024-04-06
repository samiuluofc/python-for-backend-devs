class Person():

    def __init__(self, name: str):
        self.name = name

    def eat(self, food: str):
        print(f"{self.name} is eating {food}.")


person1 = Person("Samiul")
person1.eat("rice")


class Circle():
    _PI = 3.1416  # class variable, shared among all instances of this class

    def __init__(self, cen_x: float, cen_y: float, radius: float):
        self.center = cen_x, cen_y  # tuple
        self.radius = radius

    def area(self):
        return self._PI * (self.radius**2)

    def scale(self, factor: float):
        self.radius = self.radius * factor

    def translate(self, delta_x: float, delta_y: float):
        self.center = (self.center[0] + delta_x, self.center[1] + delta_y)


c = Circle(0, 0, 10)
print(c.area())
c.scale(2)
print(c.area())
c.translate(10, 10)
print(c.area())

print(vars(c))
print(dir(c))
