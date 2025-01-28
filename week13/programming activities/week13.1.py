"""
Programming Activity 1

Write a program which gets the json from the URL: 
https://api.datamuse.com/words?rel_trg=cow (Links to an external site.) and prints the score for the word "cheese". That URL returns words related 
to the word: cow.  
- import json and requests
- create a request (req = requests(url))
- create a dictionary (dct1  = json.loads(req.text))
- loop through the dictionaries looking for the key word "cheese"
- when you find the key word cheese, print the value for keyword "score" in the same dictionary
"""