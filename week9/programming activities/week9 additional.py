"""
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

#Open the JSON file in read mode and load its content into a Python dictionary
#json.load(file)	Reads JSON directly from a file object
#json.loads(str)    Reads JSON from a string
with open("week9\programming activities\person-1.json", "r") as file:
    person = json.load(file)

print(person)
# Increment the value of "age" in dictionary by 1
person["age"] += 1

# Open the JSON file in write mode and save the updated dictionary back to the file
with open("week9\programming activities\person-1.json", "w") as file:
    json.dump(person, file)

print(person)