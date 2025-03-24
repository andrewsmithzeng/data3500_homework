"""
Write a function swap_case(sentence) that takes a sentence as input 
and returns the sentence with swapped case 
(e.g., uppercase characters become 
lowercase and vice versa). For example, swap_case("Hello World") should return "hELLO wORLD"
"""
# #solution 1:
# sentence = input('gimme a sentence:')
# print(sentence.swapcase())

#solution 2:
def swap_case():
    sentence = input('gimme a sentence:')
    result = []
    for ch in sentence:
        if ch.islower():
            result.append(ch.upper())
        elif ch.isupper():
            result.append(ch.lower())
        else:
            result.append(ch)
    return print("".join(result))

swap_case()

