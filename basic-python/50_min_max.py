# Similar to sorting: min(iterable, key=<function>)

# Has natural order
data1 = [3, 4, -5, -1, 7, -8, -90, -1, 3, -4]
data2 = ['k', 'b', 'z', 'x', 'o', 'm', 'h', 'c', 'f']
print(min(data1))
print(max(data1))

print(min(data2))
print(max(data2))

# Example: based on absolute value
print(min(data1, key=abs))
print(max(data1, key=abs))

# Example: Find the best Groom based on 'age' and 'income' (less age and more income)
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


print(max(persons, key=compare_person)["name"])
print(min(persons, key=compare_person)["name"])
