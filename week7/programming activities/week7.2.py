"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, 
but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""
colors = ['navy blue','orange','scarlet']
for _ in colors:
    print('color: ', _)
    for letter in _:
        print('letter', letter)
    print()