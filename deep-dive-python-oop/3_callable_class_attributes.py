# Callable means functions
# Attributes that can be invoked using '()' at the end


class Program:
    language = "Python"

    def say_hello():
        print(f"hello from {Program.language}")


print(Program.__dict__)
getattr(Program, "say_hello")()
Program.say_hello()
