"""
Programming Activity 3

Write a program, which loads a json file "person.json" into a Python 
dictionary. Change the contents of person["age"] by adding 1. Save the 
updated dictionary to person.json, and verify the contents of person.json 
have been updated.
- load person.json in to a Python dictionary using the json.load() function
- update the value of person["age"], increase by 1
- save the Python dictionary to person.json
- open person.json and verify the "age" value has increased by 1
"""
import json

with open('week12 unfinished\programming activities\person-2.json','r') as file:
    dic = json.load(file)
print(dic)

dic['age'] += 1

json.dump(dic,open('week12 unfinished\programming activities\person-2.json','w'))

with open('week12 unfinished\programming activities\person-2.json','r') as file:
    dic = json.load(file)
print(dic)