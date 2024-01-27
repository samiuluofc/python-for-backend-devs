"""
Conditional execution also known as Branching.
Note: python uses indentation to group together chucks of code. Its called "code blocks"
"""

price = 100

if price > 250:
    print("its costly..")
    print("Hello..")
else:
    print("price is OK.")
    print("Hello..")

# If else can be nested
if price > 250:
    print("its costly..")
else:
    if price > 100:
        print("Don't want to buy it today")
    else:
        print("Want to buy it today")

# Note: too much nesting reduce the readability. Avoid more than one nested if-else

grade = 72

letter_grade = 'F'  # Default

# However, this is in-efficient. Need if-elif
if grade >= 60:
    letter_grade = 'D'
if grade >= 70:
    letter_grade = 'C'
if grade >= 80:
    letter_grade = 'B'
if grade >= 90:
    letter_grade = 'A'
print(letter_grade)

grade = 90
# Using elif means, when the condition is satisfied, it will no longer check the remaining conditions.
if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'  # So now this is the default
print(letter_grade)
