"""
Write a function compare_strings(string1, string2) that compares two strings and returns "Equal" 
if they are equal (case-insensitive), 
"Different Lengths" if they have different lengths, 
and "Different Content" if they have the same length but different content.
"""
def compare_strings(string1, string2):
    if string1.lower() == string2.lower():
        return print("Equal")
    elif len(string1) != len(string2):
        return print("Different Lengths")
    else:
        return print("Different Content")
    

# Test cases
compare_strings('you are awesome', 'You are amazing')