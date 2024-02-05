# Note: In a dictionary, iteration order is actually follow the same order of data insertion in that dict.

person = {
    'first_name': 'Samiul',
    'last_name': 'Azam',
    'year_born': 1988
}  # Insertion order is top to bottom

for k in person:  # Iteration order is following the insertion order
    print(k)  # by default its iter through keys only

for k in person:
    print(person[k])

for k in person.keys():
    print(k)

for v in person.values():
    print(v)

for t in person.items():
    k, v = t  # tuple unpacking
    print(k, v)

for k, v in person.items():
    print(k, v)
