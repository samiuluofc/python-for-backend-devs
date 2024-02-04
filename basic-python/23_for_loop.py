for i in [1, 2, 3, 4, 5, 6, 7]:
    print(i, end=' ')
print('\n')

for i in (1, 2, 3, 4, 5, 6, 7):
    print(i * i, end=" ")
print('\n')

for ch in 'samiul':
    print(ch, end=" ")
print('\n')

for e in range(10 + 1):
    print(e * e, end=" ")
print("\n")

for i in range(4):
    for j in range(4):
        print(f"({i}, {j})", end=" ")
    print("-" * 10)
print("\n")

# enumerate function: to get the index along with the data as list of tuple.
# enumerate function is a generator (use yield instead of return)
data = [120, 23, -34, 6, -78, 89]
print(data)
data_with_index = enumerate(data)  # takes an iterable as argument
print(list(data_with_index))

for ind, value in enumerate(
        data):  # Unpacking the tuple in the for loop directly
    if value < 0:
        data[ind] = 0
print(data)

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

for suit in suits:
    print(f"{suit[0].upper()} = {suit}")

for ch in 'python':
    print(ch)

print(suit, ch)  # the variables are still accessible

for i in range(1, 20, 3):
    print(i)
print(list(range(1, 20, 3)))  # list function is doing the same as above

# Traverse through a matrix have different sizes of rows:
mat = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]

for row in range(len(mat)):  # len(mat) means number of rows
    for col in range(len(mat[row])):
        print(mat[row][col])

# simple approach than above
for row in mat:
    for data in row:
        print(data)

# Show the index number as well
for row_idx, row in enumerate(mat):
    for col_idx, element in enumerate(row):
        print(f"({row_idx}, {col_idx}) = {element}")

# Create an Identity matrix of size N
N = 10
mat = []
for i in range(N):
    mat.append([0] * N)
    mat[i][i] = 1
    print(mat[i])

# Replace None with the average of N numbers in a list
data = [12.5, None, 34.9, 40.0, 2.3, None, 10.0]
print(data)
total = 0
count = 0
for val in data:
    if val is not None:
        count += 1
        total += val

avg = total / count
print(avg)
for idx, value in enumerate(data):
    if value is None:
        data[idx] = avg

print(data)

# Note: using enumerate instead of range (to access the index) is more pythonic, that developers do.

# Replace None with the average of N numbers in a list (using list comprehension)
count = sum([1 for val in data if val is not None])  # built-in function sum
total = sum([val for val in data if val is not None])
avg = total + count
data1 = [val if val is not None else avg for val in data]
print(data1)
