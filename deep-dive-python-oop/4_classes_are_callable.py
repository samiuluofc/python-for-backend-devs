class Program:
    language = "Python"

    def say_hello():
        print(f"Hello from {Program.language}")


ob = Program()  # Callable

print(type(ob))

print(isinstance(ob, Program))

print(ob.__dict__)  # empty
print(ob.language)  # accessing class attribute, as its not in the ob.__dict__
print(Program.__dict__)
