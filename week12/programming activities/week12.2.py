"""
Programming Activity 2

Write a program which asks the user their age and favorite color.  
Store these values in a dictionary with keys "age" and "favorite_color".  
Also save the 2D list from the previous activity in the dictionary with the 
key "multiplication_table".
print all the values in the dictionary by iterating through the keys 
using a for loop.
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

dic = {}
dic['age'] = int(input('how old are you?'))
dic['favorite_color']= input('what\'s your favorite color?')
dic['multiplication_table'] = table
print(dic)

for key in dic:
    print(dic[key])