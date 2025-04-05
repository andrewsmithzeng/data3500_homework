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