# All useful builtin function.
# These are not third party modules/library (no need to pip install and import)
# These are not python standard library (no need to pip install, but need to import)

# List of all builtin functions: https://docs.python.org/3/library/functions.html

print(round(1.5))  # round to closest even if .5 (use bankers rounding)
print(round(2.5))
print(round(2.6))
print(round(1.4))

# Map function: Return an iterator that applies function to every item of iterable, yielding the results.
f = lambda a: a * a
values = [5, 20, 3, 100, 2]
gen = map(f, values)  # Gives you a generator
print(type(gen), list(gen))

para1_values = [1, 3, 4]
para2_values = [10, 20, 30]
gen = map(lambda a, b: a * b, para1_values,
          para2_values)  # Gives you a generator
print(type(gen), list(gen))

# Zip function: Iterate over several iterables in parallel, producing tuples with an item from each one.
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
list3 = [True, False, False, True]
zipped_list = zip(list1, list2, list3)  # returns iterator
print(list(zipped_list))  # now its actually done the calculation

# sorted
l = [9, 3, 2, 8, 1, 4, 2, 2, 10, 5]
s = ['samiul', 'emon', 'anik', 'nobin']
str_ = 'klnzaszehsja'
print(sorted(l))
print(sorted(l, reverse=True))

print(ord('a'))
print(ord('A'))

print(sorted(str_))
print(sorted(s))

# min and max
print(min(l))
print(min(s))
print(min(str_))

print(max(l))
print(max(s))
print(max(str_))
