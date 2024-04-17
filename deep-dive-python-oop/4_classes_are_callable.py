class Program:
    language = "Python"

    def say_hello():
        print(f"Hello from {Program.language}")


ob = Program()

print(type(ob))
print(isinstance(ob, Program))

print(ob.__dict__)  # empty
print(Program.__dict__)
