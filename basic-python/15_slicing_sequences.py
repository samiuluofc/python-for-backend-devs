"""
Slicing: seq[start:end:step], here start is inclusive whereas end is exclusive (end -1).
Slicing with steps: seq[start:end:step], step is default to 1.

Slicing always returns a new instance of that object.

Basically it follows like a loop
i = start
while (i < end):
    copy the element seq[i]
    i = i + step

default start = 0, end = len(seq) - 1 and step = 1
"""

msg = "hello samiul"
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
t1 = (1, 2, 3, 4, 5, 6, 7)

new_msg = msg[2:5]
print(new_msg, id(new_msg), id(msg))  # both are two different object
print(msg[2:])
print(msg[:6])
print(msg[:])
print(msg[:-1])
print(msg[-8:-1])

print(msg[2:10000])  # end can be outside of the index

# Slicing with steps. Default step is +1
print(list1[0:7:2])
print(list1[::2])
print(list1[7:0:-2])
print(list1[::-2])

print(msg[::-1])  # Reverse the string
print(msg[11::-1])  # Reverse the string
print(msg[-12::1])
print(msg[:-5:-1])

# tuple can also be sliced
t2 = t1[0:5]
print(t2, t1 is t2)
