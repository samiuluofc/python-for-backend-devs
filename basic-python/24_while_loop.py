"""non-deterministic looping using while loop"""

price = 100

while price > 90:
    print(f"Still waiting for price to drop. Current price is {price}")
    price -= 1
print(f"Buying price is {price}")

# Condition can be dissatisfied at the very first.
price = 50
while price > 90:
    print(f"Still waiting for price to drop. Current price is {price}")
    price -= 1
print(f"Buying price is {price}")

# Note: While loop can be goes in infinite loop
# For example: price starts with 100 and price += 1

# Remove all elements of a list until its become empty
data = [1, 2, 3, 4, 5, 6, 6, 7, 8]
while len(data) > 0:
    print(f"processing data: {data.pop()}")
print(data)

# Note: if we want to add or delete element from a List, the safest will be while loop.
# Never usr for loop. Cause add/remove changes the index dynamically.
# Also removing data from end is always easy, cause there is no need to shift data.
