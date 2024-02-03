"""
Single Responsibility principle:
    *   Also known as Separation of Concerns.
    *   If you have a class, that class should have its primary responsibility, whatever it's meant to be
        doing, and it should not take on other responsibilities.

Anti-pattern (bad pattern) is opposite of a pattern (good pattern).
"""
from datetime import datetime


class Journal:
    """
        Manage journal entires in memory (primary responsibility)
    """

    def __init__(self, name):
        self.name = name
        self.entries = []
        self.count = 0

    def add_entry(self, entry):
        self.count += 1
        self.entries.append(f"{self.count} {datetime.now().date()}: {entry}")

    def remove_entry(self, position):
        del self.entries[position]

    def __str__(
        self
    ):  # override: what your object will show if you use print/str function
        return '\n'.join(self.entries)

    '''
    def __repr__(self):
        return "This is the override of object representation"
    '''

    # Add responsibility to make a journal persistent (Its am Anti-pattern called God object (adding multiple responsibilities).
    # God object means a massive class having multiple responsibility.

    # Problem with anti-pattern: If you think about a complete application where in addition to journals, you also have other different
    # types that also need to save and load. That save and load portion will be repeat in different classes. If any
    # thing changes on saving or loading logic centrally, it will need to change in multiple places. Which is tedious and
    # time consuming, hard to manage. Better split this as a separate class that take any journal objects and prints
    # into a file.
    """
    def save(self, filename):
        f = open(filename, 'w')
        f.write(str(self)) # string representation of the object itself
        f.close()

    def load(self, filename):
        pass
    """


# Better approach: Separation of concerns
class PersistentManager():

    @staticmethod
    def save(journal, filename):  # No 'self' here as it will be a staticmethod
        """ Save any journal to a file """
        f = open(filename, 'w')
        f.write(str(journal))
        f.close()


j = Journal('My life')
j.add_entry('Nice day today')
j.add_entry('My son become 6 months today')
j.add_entry('Got my salary. Happy!!!')
print(j)
print(repr(j))  # calling __repr__() func for object j

PersistentManager.save(j, 'test.txt')

# Other notes:
# .__repr__() provides the official string representation of an object, aimed at the Developer.
# .__str__() provides the informal string representation of an object, aimed at the USER.
