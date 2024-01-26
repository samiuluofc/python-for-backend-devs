"""
Integer Division: 16 // 3 = 5 (dividend // divisor = quotient)
Float Division:   16 / 3 = 5.3333333
Mod operation:    16 % 3 = 1 (dividend % divisor = remainder)
"""
import math

print(16 // 3)  # its same as floor(16 / 3)
print(math.floor(16 / 3))
print(math.floor(3.14))  # largest integer less than 3.14
print(math.floor(-3.14))  # largest integer less than -3.14

# like floor, its similar for integer division
print(12 // 5)  # its same as floor(12 / 5), result is 2
print(-12 // -5)  # its same as floor(-12 / -5), result is 2
print(-12 // 5)  # its same as floor(-12 / 5), result is -3
print(12 // -5)  # its same as floor(12 / -5), result is -3

print(16 / 3)

# Non-intuitive behavior of % operator
# Basically its using the formula a % b = a - (b * (a // b))
print(12 % 5)
print(-12 % 5)
print(12 % -5)
print(-12 % -5)
print(12.5 % 3)  # Thats why float numbers can be used in % operation

# Moral: be careful about the impact of negative values in % and //. Make sure you understand the output.

elapsed_time = 165
hours = elapsed_time // 60
mins = elapsed_time % 60
print(f"Hours: {hours}\nMinutes: {mins}")
