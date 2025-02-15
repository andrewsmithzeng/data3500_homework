"""
Programming Activity 1

Write a program which asks the user for two numbers, stored in two variables num1 and num2. 
Generate a multiplication table for all integers 1 through num1 and 1 through num2. 
The bottom right entry in your table should have the product of num1 and num2. 
The table must be stored in a 2D list. 
The list must be created first with a nested for loop. 
Then, the table should be printed by another nested for loop iterating through the 2D list.
Steps:
- store the variables.
- create a list, and add empty lists to the list - however many your need from the variables above.
- append the values to the lists.
- use a nested for loop to iterate through the list and print the values.
"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
table = []
for i in range(1,num1+1):
    row = []
    for j in range(1,num2+1):
        row.append(i*j)
    table.append(row)

print(table)
for row in table:
    for value in row:
        print(value, end = '\t')
    print()