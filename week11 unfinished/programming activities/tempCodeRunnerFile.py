"""
Programming Activity 2

Write a program which asks the user to enter their address
Use the isalnum() function to verify the entered a valid address
- create a variable that stores the string address the user enters
- remove white space from the string
- use isalnum() on the string with no whitespace to verify all characters 
are numbers or letters
"""
address = input('could you give me your address?')

#solution 1:
testing1 = ''.join(address.split()).replace(',','').replace('.' ,'')

#Solution 2:
testing2 = address.replace('.', '').replace(' ', '').replace(',', '')

print(testing1.isalnum(),testing2.isalnum())