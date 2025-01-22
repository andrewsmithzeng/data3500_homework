"""
HW2 - Variables, Math, Output
Solutions for Chapter 2, Problems 2.3-2.8

Problem Descriptions:

2.3 (FILL IN THE MISSING CODE)
Replace *** in the following code with a statement that will print a message like 
'Congratulations! Your grade of 91 earns you an A in this course'. 
Your statement should print the value stored in the variable grade.

2.4 (ARITHMETIC)
For each of the arithmetic operators +, -, *, /, //, and **, display the value of an expression 
with 27.5 as the left operand and 2 as the right operand.

2.5 (CIRCLE AREA, DIAMETER AND CIRCUMFERENCE)
For a circle of radius 2, display the diameter, circumference and area.
Use the value 3.14159 for π. Use the following formulas (r is the radius):
diameter = 2r, circumference = 2πr and area = πr².

2.6 (ODD OR EVEN)
Use if statements to determine whether an integer is odd or even.
Hint: Use the remainder operator. An even number is a multiple of 2.
Any multiple of 2 leaves a remainder of 0 when divided by 2.

2.7 (MULTIPLES)
Use if statements to determine whether 1024 is a multiple of 4
and whether 2 is a multiple of 10.
Hint: Use the remainder operator.

2.8 (TABLE OF SQUARES AND CUBES)
Write a script that calculates the squares and cubes of the numbers from 0 to 5.
Print the resulting values in table format, using the tab escape sequence to achieve
the three-column output.

Example output:
number  square  cube
0       0       0
1       1       1
2       4       8
3       9       27
4       16      64
5       25      125
"""

# 2.3 (FILL IN THE MISSING CODE)
grade = 91  # Example grade
if grade >= 90:
    print(f'Congratulations! Your grade of {grade} earns you an A in this course')

# 2.4 (ARITHMETIC) 
print("\n2.4 Arithmetic Operations:")
print(f"27.5 + 2 = {27.5 + 2}")   # Addition
print(f"27.5 - 2 = {27.5 - 2}")   # Subtraction
print(f"27.5 * 2 = {27.5 * 2}")   # Multiplication
print(f"27.5 / 2 = {27.5 / 2}")   # Division
print(f"27.5 // 2 = {27.5 // 2}") # Integer division
print(f"27.5 ** 2 = {27.5 ** 2}") # Exponentiation

# 2.5 (CIRCLE AREA, DIAMETER AND CIRCUMFERENCE)
print("\n2.5 Circle Calculations:")
radius = 2
pi = 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2
print(f"For a circle with radius {radius}:")
print(f"Diameter = {diameter}")
print(f"Circumference = {circumference}")
print(f"Area = {area}")

# 2.6 (ODD OR EVEN)
print("\n2.6 Odd or Even:")
number = 7  # Example number
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# 2.7 (MULTIPLES)
print("\n2.7 Multiples:")
if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
else:
    print("1024 is not a multiple of 4")
    
if 2 % 10 == 0:
    print("2 is a multiple of 10")
else:
    print("2 is not a multiple of 10")

# 2.8 (TABLE OF SQUARES AND CUBES)
print("\n2.8 Table of Squares and Cubes:")
print("number\tsquare\tcube")
for i in range(6):
    square = i ** 2
    cube = i ** 3
    print(f"{i}\t{square}\t{cube}")