"""
Programming Activity 1

Write a program which can tell if a 3 digit number is a palindrome. 
 - Create a variable, which stores user input. Prompt the user to enter a 3 digit number. 
 - Convert the user input into a integer (int). To get the first digit alone, floor division by 100. 
 - To get the 3rd digit alone, modulus by 10. 
 - Check if the first digit and 3rd digit are the same. 
 - If they are the same print("palindrome!!!!"). 
 - Else print("not palindrome!")
"""
number = eval(input('Enter a 3 digit number: '))
first_digit = number//100
third_digit = number%10
if first_digit == third_digit:
    print('palindrome!!!!')
else:
    print('not palindrome!')
    