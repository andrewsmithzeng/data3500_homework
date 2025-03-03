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

with open(r"C:\Users\PandaB\OneDrive\USU\3500\data3500_homework\week9\programming activities\person-1.json", "r") as f:
    for line in f:
        print(line[10]) #打印str: {"name": "Robert Downey Jr.", "age": 60, "birthday": "April 4"} 的第10个字符，即R

import json
with open(r"C:\Users\PandaB\OneDrive\USU\3500\data3500_homework\week9\programming activities\person-1.json", "r") as f:
    for line in f:
        data = json.loads(line)  # 解析 JSON 数据为 Python 字典
        print(data) #打印 dictionary: {'name': 'Robert Downey Jr.', 'age': 60, 'birthday': 'April 4'}
        print(data["age"]) #打印 dictionary 中的 "age" 值，即60   