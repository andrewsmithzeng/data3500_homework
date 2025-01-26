"""
2. Write a Python program to reverse a given three or more digit integer WITHOUT using lists 
(hint, use // and % to isolate numbers)
"""
#without using list
number = int(input('give me a three or more digit integer:'))
reversed_number = 0
sign = 1 if number >0 else -1

while number != 0:
    last_digit = number % 10
    number //= 10
    reversed_number = reversed_number*10 + last_digit

print(f'the reversed integer is {reversed_number}.')



#using list
# Input: Get a three or more digit integer from the user
num = input("Enter a three or more digit integer: ")

# Convert the input to a list of characters
num_list = list(num)

# Reverse the list
reversed_list = num_list[::-1]  # Use slicing to reverse the list

# Join the reversed list to form the reversed number
reversed_num = ''.join(reversed_list)

# Print the reversed number
print(f"The reversed number is: {reversed_num}")
