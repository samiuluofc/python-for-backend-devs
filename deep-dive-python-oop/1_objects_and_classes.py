class Person:
    pass


# class itself is an object of class 'type'
print(type(Person))
print(type(type))
print(help(type))  # its a class
print(isinstance(Person, type))

# Already have built-in attributes and functions
print(Person.__name__)

# still callable
ob = Person()
print(type(ob))
print(ob.__class__)
print(isinstance(ob, Person))
print(isinstance('hello', str))

# str is also a class
print(type(str))
