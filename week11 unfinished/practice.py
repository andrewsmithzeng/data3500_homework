"""
1. You are given a dictionary representing products and their 
prices: {"apple": 0.99, "banana": 0.75, "orange": 1.25, "grapes": 1.50}. 
Write a Python program that calculates the total price of items 
in a user's shopping cart. The user can enter items and quantities 
until they are done, then calculate and print the total price.
"""

"""
2. Create a Python generator that generates prime numbers indefinitely. 
Write a program that uses this generator to find the first 100 
prime numbers and calculate their sum.
"""

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
5. Write a Python program that generates a list of random numbers 
between 1 and 100. Use list comprehension to create a new list 
containing only the even numbers from the generated list.
"""

"""
Using a function rand5() that returns an integer from 1 to 5 
(inclusive) with uniform probability, implement a function 
rand7() that returns an integer from 1 to 7 (inclusive).
"""

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