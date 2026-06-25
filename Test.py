# How do you make a string variable?
# Strings are always in quotes. You can use "" or ''
# Also, to assign values to variables, you need an equals sign =
random_string ="pokemon"

# make two new variables, one storing a float and one an integer
# `int` and `float` are both *keywords* in Python, which means they
# CANNOT be used as variable names. But literally any other name would work.
example_int = 21
example_float = 2.1

# last basic data type is boolean
example_bool = True

# example print statement
print(random_string)
print(example_int)
print(example_float)
print(example_bool)


# How about arithmetic operators?
# Give examples of using +, -, *, /
print(1+2-1*3/4)

# Do you know what these are:   //   %   **
# // is called integer or floor division
print(7 // 3)

# % is called modulo and gives the remainder of division
print(7 % 3)

# ** is for exponents
print(2**4)


# Comparison Operators
# ==     !=      >      <       >=       <=
zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5

if one == (three - two):
    print("3 - 2 = 1")
if two != four:
    print("two does not equal four")

print()

# LOOPS: `for` loops and `while` loops
# FOR loops are best for going through a known sequence, like a list of things
# WHILE loops are best for repeating something until a condition becomes false

example_list = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
print("fourth element: ", example_list[3])
print()

for number in example_list:
    print(number)

length_of_example_list = len(example_list)
print("range(10): ", range(10))
for i in range(length_of_example_list):
    print(example_list[i])

print()
print("even numbers in example_list:")
for number in example_list:
    if number % 2 == 0:
        print(number)

print()
print("WHILE LOOPS")
finished = False
num = 0

while not finished:
    print(num)
    num += 3
    if num > 27:
        finished = True

# Tuples?
# Tuples are just lists, but you can't change anything inside them
example_tuple = (0, 3, 6, 9)