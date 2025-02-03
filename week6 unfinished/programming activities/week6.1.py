"""
Programming Activity 1

Write a function named "welcome_fctn" which takes one argument, called "name". 
 Inside the function, print to the console "Welcome " + name.
- Use the def command to define a function "welcome_fctn"
- Add a parameter list with one variable "name", i.e. (name)
- Print "Welcome "+ name in the function body.
- We don't need a return statement here, but keep in mind python does return nothing.
- Call the function, welcome_fctn(<your_name>)
"""

def welcome_fctn(name):
    print( f"Welcome {name}.")
    

welcome_fctn("Andy")    