import math

## Calculate magnitude of N vectors
vec = [(1, 1), (2, 2), (3, 4), (5, 8)]

# Using loop
magnitude1 = []
for item in vec:
    magnitude1.append(math.sqrt((item[0]**2) + (item[1]**2)))

# Using list comprehension
magnitude2 = [math.sqrt((item[0]**2) + (item[1]**2)) for item in vec]

print(magnitude1)
print(magnitude2)

## Gather words with length greater than 3
words = 'Python is an awesome language'.split()
print(words)
long_words = [word for word in words if len(word) > 3]
print(long_words)

# Gather the high sales (> 10) product from a dictionary
product_journal = {'watch': 20, 'book': 5, 'toys': 100, 'food': 200}

products = [
    product for product, count in product_journal.items() if count > 10
]
print(products)

# Creation of 3 by 3 zero matrix
zero_mat = [[0] * 3] * 3
print(zero_mat)
zero_mat[0][0] = 100
print(zero_mat)  # Its actually repeated same object 3 times
print(id(zero_mat[0]), id(zero_mat[1]),
      id(zero_mat[2]))  # all have same reference

# However, using comprehension will not repeat same object. Expression part is always evaluated
zero_mat = [[0] * 3 for _ in range(3)]
print(zero_mat)
print(id(zero_mat[0]), id(zero_mat[1]),
      id(zero_mat[2]))  # all have different reference

# create an identity matrix using nested list comprehension
# Note: NESTED CAN BE LESS READABLE

identity_mat = [[1 if row == col else 0 for col in range(3)]
                for row in range(3)]
# Here row variable is accessible in the inner loop/list
print(identity_mat)

# However, regular nested loop is more readable in this case
identity_mat = []
for row in range(3):
    inner_mat = []
    for col in range(3):
        n = 1 if row == col else 0
        inner_mat.append(n)
    identity_mat.append(inner_mat)
print(identity_mat)
print(id(identity_mat[0]), id(identity_mat[1]), id(identity_mat[2]))
