"""

We will be using context manager to open and close a file.

A context is an area of code that is entered and exited.
It is entered by calling a context manager using a with statement.
It is exited when the with code block is exited.

Context manager is responsible for
* running some code on entry
* running some code on exit

The exit portion will run always regardless of its naturally exited or error exit.

That is why its perfect for open and close a file.

# Open a file
file_object = open(filepath, mode) # mode can be 'r', 'w', 'a' (read, write, append)
file_object.readlines()
file_object.close() # We always need to close a file

Why closing is needed
* Release the resources (os dont allow tons of file to be opened)
* writes are often buffered until the file is closed (data loss).

What happens if exception happens during write/read a file. We can use try, except and finally.
But much easier is to use the context manager (open is also a context manager).
"""

file = open("test.txt", 'r')  # file object

print(file.name)
print(file.readable())  # is readable
print(file.writable())  # is writable
print(file.closed)  # is closed
file.close()
print(file.closed)

file = open("test.txt", 'r')  # file object
data = file.readlines(
)  # read all lines at a time, returns as a list of string
file.close()
print(len(data))  # list of strings (each line)
print(data)

# We can read one line at a time.
# File object is an iterator.

file = open("test.txt", 'r')  # file object
for line in file:
    print(line, end='')
file.close()

file = open("test.txt", 'r')  # file object
print(next(file), end='')
print(next(file), end='')
print(next(file), end='')
print(next(file), end='')
#print(next(file)) # For some reason (exception) we never hit the file close. So that means its still open.
file.close()

# So we can use try and finally
try:
    file = open("test.txt", 'r')  # file object
    while True:
        print(next(file), end='')
except:
    print("Exception happened")
finally:
    print("Closing file ...")
    file.close()
print(file.closed)

# There is a cleaner way using the python context manager
# open is actually a context manager
with open("test.txt", 'r') as file:  # open a file during entering the context
    print(next(file), end='')
    print(next(file), end='')
    print(next(file), end='')
    print(next(file), end='')
print(file.closed)
