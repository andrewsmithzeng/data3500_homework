# WHAT DOES THIS CODE DO? Create the variables x = 2 and y = 3, then determine what each of the following statements displays:
x = 2
y = 3
print('x =', x)
print('Value of', x, '+', x, 'is', (x + x))
print('x =')
print((x + y), 'x =', (y + x))


"""
Write a Python function that takes input from the user for three numbers, compares them using dynamic typing, 
and outputs the smallest and largest numbers. Then, if the largest number is divisible by 2, print the range 
between the smallest and largest numbers. If the largest number is not divisible by 2, print whether the 
smallest number is within the range of 0 to 10.
"""
def number_comparison():
    a = eval(input('please give me the fisrt number:'))
    b = eval(input('please give me the second number:'))
    c = eval(input('gimme one more:'))
    biggest = max(a,b,c)
    smallest = min(a,b,c)
    print(f'the biggest number is {biggest} and the smallest one is {smallest}')
    if biggest % 2 == 0:
        print(f"the range between the smallest and the largest numbers is {biggest - smallest}.")
    else:
        if smallest in range(10):
            print('the smallest one is between 0~10')
        else:
            print('we get the smallest number outside of 0~10')

number_comparison()

