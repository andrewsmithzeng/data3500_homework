"""
Given a list of strings representing names, 
write a list comprehension to create a new list containing only the names that start with a vowel (a, e, i, o, u). 
Additionally, transform these names to uppercase. Finally, return both the new list and the count of names in it. 
If no names meet the criteria, return an empty list and a count of 0.

names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Charlie"]
"""

names = ["Alice", "Bob", "Eve", "Oscar", "Uma", "Charlie"]
lst = [x for x in names if x[0].lower() in ['a','e','i','o','u']]
print(lst,len(lst)) 