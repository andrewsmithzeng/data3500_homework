"""
Programming Activity 2

Write a Python program that takes a list of strings as input, where some strings might have leading or trailing spaces. 
Use list comprehension to remove these spaces from each string in the list.
"""
strings = ["   hello  ", "whitespace      ", "   :)  "]

lst = [x.strip() for x in strings]
print(lst)