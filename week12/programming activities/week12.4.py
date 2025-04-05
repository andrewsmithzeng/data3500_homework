"""
Programming Activity 4

Write a program that asks the user for two numbers. In a try statement, 
attempt to divide number 1 by number 2.  If number 2 is a 0, print a 
message in the except statement saying "Error, attempted to divide by zero"
- create two variables, inputted by the user
- in a  try: block attempt to divide num1 by num2
- in a except: block print a message indicating divide by zero error
- end program
"""
num1 = eval(input("gimme a number:"))
num2 = eval(input("gimme another number:"))
try:
    print(f'{num1} divided by {num2} equals to {num1/num2:.2f}.')
except:
    print('Error, attempted to divide by zero')


