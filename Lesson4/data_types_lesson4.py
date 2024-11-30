# string data type

# literal assignment
import math
first = "Sadiq"
last = "Abdul"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)
fullname += '!'
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)
statement = "I like rock music fro the " + decade + "s."
print(statement)

# multiple lines
multiline = '''
Hey there

I was there

            you?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("you", "ok"))
print(multiline)


print(len(multiline))
multiline += "                "
multiline = "             " + multiline

print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print('')
# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print('')
# String index values
print(first[1])
print(first[-1])  # last value in the index
print(first[1:-1])  # without 1st and last
print(first[1:])


# Some methods return boolean data
print(first.startswith("S"))
print(first.endswith("q"))


# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.34)
print(type(gpa))
print(isinstance(gpa, float))
# complex type
com_value = 5+3j
print(type(com_value))
print(com_value.real)
print(com_value.imag)

# Built-in functions for numbers

print(abs(gpa))

print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
print(type(zipcode))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
