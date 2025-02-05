"""
Programming Activity 2

Update the function in activity one, and create a new string variable in the function called, welcome_message. 
The variable welcome_message should be assigned the value "Welcome "+ name. 
The same value printed in activity 1, but here you save it as a variable. Return the variable welcome_message.
- Assuming your function in programming activity 1 works, you will need to:
- Create a variable to store "Welcome " + name
- Return the value welcome_message
- There are a couple ways to test this. you could
         1. Print(welcome_fctn("Bob"))
         2. Create a variable to store what is returned by the function then print that
"""
def welcome_fctn(name):
    welcome_message = f"Welcome {name}."
    return welcome_message 

print(welcome_fctn("Andy"))

    