"""
Programming Activity 3

Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. 
Use if statements and the Boolean variables created above to print a message 
to the user whether or not the child may sit in the front seat.
"""
age = eval(input('How old is your kid?'))
weight = eval(input("What's the weight of your child?"))
# Boolean variables for the criteria

is_12_or_older = age >= 12
is_11_and_over_90 = age == 11 and weight > 90
is_under_11_and_over_100 = age < 11 and weight > 100

#Determine if the child can sit in the front seat
can_sit_in_front = is_12_or_older or is_11_and_over_90 or is_under_11_and_over_100

# Output the result
if can_sit_in_front:
    print("The child may sit in the front seat.")
else:
    print("The child may not sit in the front seat.")
