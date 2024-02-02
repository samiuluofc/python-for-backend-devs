"""
Build string with string and other types of variables
"""

# Concatenation (Tedious and error prone approach)
income = 100_000
members = 3
msg = 'A family with ' + str(members) + ' members need at least ' + str(
    income) + '$ yearly income.'
print(msg)

# format function
msg = 'A family with {} members need at least {}$ yearly income.'
print(msg.format(members, income))  # need to maintain the order of arguments

msg = 'A family with {x} members need at least {y}$ yearly income.'
print(msg.format(y=income, x=members))

# f string (best approach cause we dont need to know the order of arguments)
msg = f'A family with {members} members need at least {income}$ yearly income.'
print(msg)

# display float numbers in f string
pi = 22 / 7
print(f"Value of PI is {pi}")
print(f"Value of PI is {pi:.4f}")
