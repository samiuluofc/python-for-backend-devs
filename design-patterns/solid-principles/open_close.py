"""
Open Close principle:
    *   A class should be open for extension (inheritance) but closed for modification.
    *   Classes should be closed for modification, which means that after you've written
    and tested a particular class, you should not modify it. Instead, you should extend it.

Specification pattern:

"""
from enum import Enum


class Color(Enum):  # Enum is the base class
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# Not a good approach, cause manager will ask you to add more filter.
# Products will have more features like color and size.
# filter can be based on any combination of product features/criteria.
class ProductFilter():

    @staticmethod
    def filter_by_color(products, color):
        for p in products:
            if p.color == color:
                yield p

    @staticmethod
    def filter_by_size(products, size):
        for p in products:
            if p.size == size:
                yield p

    @staticmethod
    def filter_by_size_and_color(products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p

    # We can keep adding filters based on different combination of features/criteria.
    # This approach does not scale. And in addition to breaking the open closed principle,
    # you're also causing something called a 'state space explosion'.


# Solution that obeys 'open close' principle, as well as solved the 'state space explosion'
# We are going to use specification pattern


# Acting as an abstract base class (no implementation).
# Need to override.
class Specification():
    """determines whether or not a particular item satisfies a particular"""

    def is_satisfied(self, item):
        pass


# Acting as an abstract base class (no implementation).
# Need to override.
class Filter():

    def filter(self, items, spec):
        pass


# Instead of modifying any of these classes, we are going extends (inherit) them, to create new class.
class ColorSpecification(Specification):  # extends

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):  # override
        return item.color == self.color


class SizeSpecification(Specification):  # extends

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):  # override
        return item.size == self.size


# So we can create as much as possible Specification class based on product features/attributes
class BetterFilter(Filter):  #extends

    def filter(self, items, spec):  # override
        for item in items:
            if spec.is_satisfied(item):
                yield item  # its become a generator (due to yield)


if __name__ == '__main__':  # in case we want to use this file as a module, this if will be false then

    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]  # create the product lists

    # Create the specifications first
    green = ColorSpecification(Color.GREEN)
    large = SizeSpecification(Size.LARGE)

    bf = BetterFilter()

    print("Filter by color GREEN:")
    for p in bf.filter(products, green):
        print(f"{p.name} is green")

    print("Filter by size LARGE:")
    for p in bf.filter(products, large):
        print(f"{p.name} is large")

# That means if new features/attributes added to the Product class,
# We will just create a new Specification class like Color or Size. Then do the filter.
# This approach is not going to modify any of the specification or Filter class.
