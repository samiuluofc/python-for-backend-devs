"""
Proper close of a file is even more important after writing,
cause new data stays in flash/memory until you close the file, and then it saved to disk.
So best use a context manager.

'w' or 'a' will create the file if it does not exist.

Write operations never add \n automatically at the end of line. So we are responsible to do that.

"""

with open('test1.txt', 'w') as f:
    f.write("Samiul\n")  # takes a single string
    f.writelines(["Emon\n", "anik\n", "nobin\n"])  # takes a list of string

with open('test1.txt', 'r') as f:
    print(f.read())

with open('test1.txt', 'a') as f:
    f.write("Samiul\n")  # takes a single string
    f.writelines(["Emon\n", "anik\n", "nobin\n"])  # takes a list of string

with open('test1.txt', 'r') as f:
    print(f.read())
