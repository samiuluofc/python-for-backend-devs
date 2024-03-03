"""
Similar to filter function: takes in an iterable and key function.
Key function takes an element from iterable and returns a value that will be used for comparison.
The sort will be based on the value return from the key function.
The values that return from the key function must have natural sort order (numbers and strings).

"""

# Following have natural sort order, so we dont need to provide key function
data1 = [3, 4, -5, -1, 7, -8, 9, -1, 3, -4]
data2 = ['a', 'b', 'z', 'x', 'o', 'm', 'h', 'c', 'f']
print(sorted(data1))
print(sorted(data1, reverse=True))
print(sorted(data2))
print(sorted(data2, reverse=True))

# Sort numbers based on their absolute value
key_func = lambda x: abs(x)
print(sorted(data1, key=key_func))
print(sorted(data1, key=key_func, reverse=True))

# Note: Python use Tim Sort (derived from merge sort and insertion sort) under the hood
# Note: Time Sort is an stable sort (it retained the order of the initial data if two values are same)

# Example: Sort list of dicts based on based on 'age' and 'income' (more age and less income come first)
persons = [{
    "name": "samiul",
    "age": 30,
    "income": 123_000
}, {
    "name": "anik",
    "age": 25,
    "income": 200_000
}, {
    "name": "karim",
    "age": 50,
    "income": 250_000
}]


def compare_person(person):
    # For each year after 20, there will 5_000 penalty
    penalty = (person["age"] - 20) * 5_000
    return person["income"] - penalty


print(sorted(persons, key=compare_person))

# Example 1: Case insensitive sorting of words without modifying the original data list
# Example 2: Sort words based on their length

data = ["Samiul", "zOHRA", "EmoN", "emon", "azam", "AzAm", "Zohra", "samiul"]
print(sorted(data))
print(sorted(data, key=lambda word: word.lower()))  # Case-less sorting
print(sorted(data, key=len))  # length based sorting
