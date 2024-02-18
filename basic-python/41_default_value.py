# Its simply a default value for an argument. If no value is provided for the argument, the default will be used.
# once we define a default argument, we need to define it for everyone afterwards


def func(a=1):  # Default value is 1 for a
    print(a)


func(10)
func()


def my_func(a, b=10, c=20):
    print(a, b, c)


my_func(200)
my_func(200, 100)
my_func(200, c=100)
my_func(c=100, a=300)


def is_close(a, b, abs_tol=0.01):
    return abs(a - b) <= abs_tol


print(is_close(12.34, 12.33))
print(is_close(12.34, 12.36))
print(is_close(12.34, 12.36, abs_tol=1))


def parse(txt, sep=',', strip=True):
    items = txt.split(sep)
    if strip:
        return [item.strip() for item in items]
    else:
        return items


print(parse('  a, b   , c   '))
print(parse(' a|b|c ', sep='|'))
print(parse(' a: b: c: ', sep=':', strip=False))
print(parse(' a: b: c: ', sep=':'))

# Print function also have some default parameters, we can actually put arguments on those parameters
print('a', 'b', 'c')  # sep is default to space, and end is '\n'
print('d')
print('a', 'b', 'c', sep='--',
      end='**\n')  # sep is default to space, and end is '\n'
print(
    *'abc', sep='--', end='**\n'
)  # unpacking iterable 'abc'. Print function takes variable length args as well.


# problem decomposition with multiple function:
def process_row(row, item_sep):
    return item_sep.join(
        (str(ele) for ele in row))  # a generator instead of list comprehension


def process_data(data, item_sep=',', line_sep='\n'):
    processed_rows = (process_row(row, item_sep)
                      for row in data)  # a generator
    return line_sep.join(processed_rows)  # join needs an iterable


data = [[10, 20, 30], [40, 50, 60], [700, 800, 900]]
print(process_data(data))
print(process_data(data, item_sep='-', line_sep='|'))
