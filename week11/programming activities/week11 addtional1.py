"""
Write a Python program that takes a sentence as input and checks if it's a palindrome. 
Ignore spaces, so that phrases like "A man a plan a canal Panama" are considered palindromes.
"""

sentence = list(input("Enter a sentence: ").replace(' ', '').lower())
print('it is a palindrome' if sentence == sentence[::-1] else 'it is not a palindrome')

#solution 2:reversed('str') returns an iterator:<reversed object at 0x...>
sentence = input("Enter a sentence: ").replace(' ', '').lower()
print('it is a palindrome' if sentence == ''.join(reversed(sentence)) else 'it is not a palindrome')