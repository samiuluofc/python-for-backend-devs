"""
Method (function attribute is bound to the object).
Bound method (Unlike a function it is bound to an object).
That object is always passed as a first parameter.

instance method vs class method
Method vs function

ob.method() is equivalent to Class.method(ob)

So method is actually an object that consist of the
* a class instance/object
* a function

Like any object it (method) has many attributes:
__self__ "the instance the method bound to"
__func__ "the original function"

SO calling ob.method(parameter) is equivalent of method.__func__(method.__self__, parameters)

Instance method needs a parameter (first parameter: self) to pass the object reference.
Class method dont need that. But to make it bound to the class we can have it (cls).

"""


class Person():

    def say_hello():
        print("Hello...")


print(type(Person.say_hello))

p = Person()
print(type(p.say_hello))

# TypeError: Person.say_hello() takes 0 positional arguments but 1 was given
#p.say_hello()


class Person2():

    def say_hello(self, name):
        self.name = name
        print(f"Hello...{self.name}")


p = Person2()
print(hex(id(p)))
p.say_hello("samiul")
print(p.name)
Person2.say_hello(p, "emon")
print(p.name)
print(p.__dict__)

# methods have attribute
method_hello = p.say_hello
print(type(method_hello))
print(method_hello.__func__)
print(method_hello.__self__)

# Monkey patching


class Person3():

    def say_hello(self):
        print(f"instance method called from {self}")


p = Person3()
print(hex(id(p)))
print(Person3.say_hello(p))
print(p.say_hello())

# monkey patched the class
Person3.do_work = lambda self: f"do work called from {self}"
print(p.do_work())
