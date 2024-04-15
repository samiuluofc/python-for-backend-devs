# class attributes, not the attributes of an instance


class Program:
    "doc string for this class"
    language = 'python'
    version = "3.12"


print(Program.language, Program.version)
print(getattr(Program, 'language', None), getattr(Program, 'version', None),
      getattr(Program, 'non-exist', None))
Program.language = 'C++'
Program.version = '2023'

# Python is dynamic language
setattr(Program, 'creator', 'Bjarne Stroustrup')

print(getattr(Program, 'language', None), getattr(Program, 'version', None),
      getattr(Program, 'creator', None))
delattr(Program, 'creator')
print(getattr(Program, 'language', None), getattr(Program, 'version', None),
      getattr(Program, 'creator', None))

# Read only dictionary
print(Program.__dict__)
print(Program.__dict__['language'])
print(Program.__dict__.keys())
print(Program.__doc__)

# Note: not all attributes are in the dict. For example __name__ is not in this dict

ob1 = Program()
ob2 = Program()

# Class attributes are common properties between instances of that class
# Changes to this attributes at class level will impact all instances of it
print(ob1.language)
print(ob2.language)

Program.language = 'Python'
print(ob1.language)
print(ob2.language)

ob1.language = 'java'
print(ob1.language)
print(ob2.language)
