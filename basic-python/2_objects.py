"""
objects: entities contains its state (data) and methods (functionality).
This is also know as encapsulation in Object oriented programming.

Also the state and the methods are also known as attributes. We
use dot notation to use those attributes.

Mutable: An object is mutable if its internal states (one or more) are changeable.
In python many data types are immutable such as integer, float, boolean, string, tuple etc.
Some are mutable, such as set, dictionary and lists.

Any data type we have in python is actually an object.
"""

# integer data is the 10, and its functionality is __add__ (double under score OR dunder or magic method).
# 10 + 100 is an operator overloading for '+', which actually call __add__ method.
print((10).__add__(100))

print((.125).as_integer_ratio())  # float is also object
print((.1).as_integer_ratio())  # float is also object


# creating custom object/class
class Account:

    def __init__(self, account_type, account_number, account_balance):
        self.balance = account_balance
        self.number = account_number
        self.type = account_type

    def get_account_info(self):
        """ Get account info
        """
        return (self.number, self.type, self.balance)  # return a tuple


acc_obj = Account("savings", "A898-345-Hj23", 1000.00)
print(acc_obj.balance)
print("Account number:", acc_obj.get_account_info()[0])
print(type(acc_obj))
