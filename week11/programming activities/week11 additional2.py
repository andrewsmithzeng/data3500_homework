
"""
 Write a program that takes a sentence as input and reverses the words in the sentence 
 without changing the order of words but removing any leading or trailing spaces.
"""

sentence = input("Enter a sentence: ").split()
#solution1:
reversed_sentence1 = " ".join([i[::-1] for i in sentence])
print(reversed_sentence1)
#solution2:
reversed_sentence2 = " ".join([''.join(reversed(i)) for i in sentence])
print(reversed_sentence2)
