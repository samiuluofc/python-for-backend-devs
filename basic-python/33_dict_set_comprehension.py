# Dictionary comprehension { key: value for item in iterables if expr}
# Set comprehension { expr for item in iterable if expr}

import string
from collections import Counter

# Dict comprehensions
products = ['books', 'toys', 'cloths', 'watches']
inventory_count = [2, 50, 20, 10]

dict_inventory = {
    prod: inventory_count[ind]
    for ind, prod in enumerate(products) if inventory_count[ind] >= 5
}

print(type(dict_inventory), dict_inventory)

# Set comprehensions
# Create a set of unique words from a paragraph where len of each word is > 4

para = """
    Elon Musk is the CEO of electric-vehicle maker Tesla,
    whose board he joined in 2004. During his nearly two
    decades there, the company has grown to be the global
    leader in EVs and world’s most valuable car company.
    Musk is also CEO and founder of SpaceX, and in 2022,
    he purchased Twitter for $44 billion. The entrepreneur,
    one of the world’s wealthiest people, has also launched
    other ventures including Neuralink, a brain-computer
    startup and Boring Co., a tunneling company. More recently
    he has incorporated a company called X.AI as part of
    efforts to steer development of artificial intelligence.
"""

for ch in string.punctuation:
    para = para.replace(ch, ' ')

print(para)
para = para.lower()
print(para)
list_words = para.split()

result = {word for word in list_words if len(word) > 4}
print(type(result), len(result))
print(result)

# Frequency count of characters
dict_count = {key: len([ch for ch in para if ch == key]) for key in set(para)}
print(dict_count)

# Frequency count using builtin module
dict_count1 = Counter(para)
print(dict_count1)
print(dict_count1 == dict_count)
print(dict_count == dict_inventory)  # Just a equal test
