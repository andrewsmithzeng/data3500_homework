"""
1. You are given a dictionary representing products and their 
prices: {"apple": 0.99, "banana": 0.75, "orange": 1.25, "grapes": 1.50}. 
Write a Python program that calculates the total price of items 
in a user's shopping cart. The user can enter items and quantities 
until they are done, then calculate and print the total price.
"""
prices_dictionary = {"apple": 0.99, "banana": 0.75, "orange": 1.25, "grapes": 1.50}

def totalprice(apple, banana, orange, grapes):
    apple = int(input("Enter the number of apples: "))
    banana = int(input("Enter the number of bananas: "))
    orange = int(input("Enter the number of oranges: "))
    grapes = int(input("Enter the number of grapes: ")) 
    total_price = 0
    total_price += prices_dictionary["apple"] * apple
    total_price += prices_dictionary["banana"] * banana
    total_price += prices_dictionary["orange"] * orange
    total_price += prices_dictionary["grapes"] * grapes
    return total_price
"""
2. Create a Python function that returns prime numbers. 
Write a program that uses this generator to find the first 100 
prime numbers and calculate their sum.
"""

for i in range(1,100000000):
    pass
"""
3. Write a Python program that reads a text file containing a 
list of numbers, computes the mean and standard deviation 
of the values, and writes the results to an output file. 
Use the file provided on Canvas: numbers.txt
(hint, use the statistics module: statistics.stdev(data_variable) )
"""
import statistics


"""
4. Write a Python program that takes a sentence as input and counts 
the number of vowels and consonants in the sentence. Ignore 
spaces and consider case-insensitive matches.
"""

"""
5. Write a Python program that generates a list 100 elements long 
of random numbers between 1 and 100. Use list comprehension to 
create a new list containing only the even numbers from the 
generated list.
"""
import random
lst = [random.randint(1,100) for i in range(100)]
print(lst)
lst_even = [i for i in lst if i % 2 == 0]
print(lst_even)   
"""
6. Write a Python function that takes a string as input and checks 
if it is a palindrome (reads the same backward as forward). 
Ignore spaces, punctuation, and consider case-insensitive matches.
Test your function on the following strings:
"Sit on a potato pan, Otis."
"Cigar? Toss it in a can. It is so tragic."
"Go hang a salami, I'm a lasagna hog."
"""

strings_to_test = [
    "Sit on a potato pan, Otis.",
    "Cigar? Toss it in a can. It is so tragic.",
    "Go hang a salami, I'm a lasagna hog."
]

def is_palindrome(string):
    string = ''.join(string.split(' ').strip('?.,')).lower()
    return string == string[::-1]
for string in strings_to_test:
    print(is_palindrome(string))

"""
7. Run-length encoding is a fast and simple method of encoding 
strings. The basic idea is to represent repeated successive 
characters as a single count and character. For example, the 
string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume 
the string to be encoded have no digits and consists solely 
of alphabetic characters. You can assume the string to be 
decoded is valid.
"""

"""
8. You are given a list of dictionaries representing 
students' information (name, age, and grade). 
Write a Python program to calculate the average age of 
students and the highest grade among them.
"""
students = [
    {"name": "Alice", "age": 18, "grade": 85},
    {"name": "Bob", "age": 17, "grade": 92},
    {"name": "Charlie", "age": 19, "grade": 78}
]

"""
9. Write a Python program that takes a list of integers as 
input and rearranges the elements in the list in such a 
way that all even numbers appear before odd numbers. 
Preserve the order of even and odd numbers in the original list.
"""

input_list = [1, 4, 2, 7, 5, 8, 10]

# output list: [4,2,8,10,1,7,5]