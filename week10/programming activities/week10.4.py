"""
Programming Activity 4

Create a variable that stores the sentence below, and print the sentence to 
the console, before making any changes. Change the first letter in the 
sentence to be capitalized. Change the first instance of Whoa to be whoa 
(all lower case), and the second instance of Whoa to be WHOA(all upper case).  
Append a exclamation point to the end of the sentence. 
Then re-print the sentence to the console.

sentence = "dude, I just biked down that mountain and at first I was like 
Whoa, and then I was like Whoa"
 - using the string variable sentence, change the first letter to upper 
   case using capitalize()
 - create a list called "words" that stores all the words in the sentence 
   in a list using the split() function.
 - change the first "Whoa" to "whoa", and the second "Whoa" to "WHOA".
 - append an exclamation point.
 - print the new sentence.
"""
sentence = "dude, I just biked down that mountain and at first I was like Whoa, and then I was like Whoa."
words = sentence.split(' ')
words[0] = words[0].capitalize() 
print(words)

'''
#Solution 1:
index = [i for i, word in enumerate(words) if 'whoa' in word]
print(index)
words[19] = "WHOA!"
'''
#Solution 2:
count = 0
for i, word in enumerate(words):
    if 'Whoa' in word:
        count += 1
        if count == 1:
          words[i] = words[i].lower()
        elif count == 2:
            words[i] = 'WHOA!'

sentence2 = ' '.join(words)
print(sentence2)