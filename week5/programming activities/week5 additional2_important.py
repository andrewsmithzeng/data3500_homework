"""
1. Write a Python program that checks the strength of a user's password. Password strength is determined by the following rules:

The password must be at least 8 characters long.
The password must contain at least one uppercase letter.
The password must contain at least one lowercase letter.
The password must contain at least one digit.
The password may contain special characters (e.g., !, @, #, $, etc.), but it is not required.## not char.isalnum()
Your program should prompt the user to enter a password, and then it should determine whether the password meets these criteria.

Example Input/Output:
# Input
password = "SecureP@ssw0rd"
# Output
Password is strong!

# Input
password = "weak"
# Output
Password is weak. It does not meet the criteria.
"""
uppercase, lowercase, digit = False, False, False

password = input("Enter your password: ")

#cheak each character in one loop
for char in password:
    if char.isupper():
        uppercase = True
    elif char.islower():
        lowercase = True
    elif char.isdigit():
        digit = True
    
    # 若所有条件都已满足，可提前终止遍历
    if uppercase and lowercase and digit:
        break

#directly use boolean expression to determine True or False
length = len(password) >= 8


if uppercase and lowercase and digit and length:
    print("Password is strong!")
else:
    print("Password is weak. It does not meet the criteria.")
