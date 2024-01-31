"""
Unicode: assigning a code to a character (code points: numerical value of a character).
It does not specify how to encode the code point in binary format.

UTF-8 (Unicode Transformation Format): Does the encode (binary format) for code point. There are others such as UTF-16, UTF-32 etc.
In python default is UTF-8.

So, Unicode and UTF is two different things.

List of Unicode:
[A] https://www.compart.com/en/unicode/U+0041
[α] https://www.compart.com/en/unicode/U+03B1
[🐍] https://www.compart.com/en/unicode/U+1F40D
"""

print(ord('🐍'))  # integer value
print(hex(ord('🐍')))  # hex value
print(int('03B1', 16))  # convert a hex number int int

α = 'samiul'  # using this as a variable.
print(α)
# However, we cannot use the snake as the variable as its
# a different type of unicode letter/symbol
# In general we should not use them as variable name.

# Use escape sequence to inject in a string
var = "\N{Latin Capital Letter A}n apple."  # Name escape
print(var)

var = "\u0041n apple."  # Unicode escape, need to exact 4 digits after \u
print(var)

var = "\U0001F40Dnake."  # Need to have 8 digits after \U
print(var)

var = "...\U0001F600..."  # Need to have 8 digits after \U
print(var)

var = "...\N{Grinning Face}..."  # Name escape
print(var)
