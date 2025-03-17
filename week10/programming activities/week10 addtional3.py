"""
 Write a function count_title_case(sentence) that takes a sentence as input 
 and returns the number of words in title case (first letter of each word capitalized). 
 For example, count_title_case("Python is an Amazing Programming Language") should return 4.
"""
def count_title_case():
    sentence = input('gimme a sentence:').split() #split() method splits a string into a list
    count = 0
    for word in sentence:
        if word == word.capitalize():
            count += 1
    return print(count)

count_title_case()
    

# sentence = input('gimme a sentence:').split()
# print(sentence)