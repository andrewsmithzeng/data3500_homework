"""
HW3 - If statements, Loops, Logic
50 points

3.4 (Fill in the Missing Code)
for ***:
    for ***:
        print('@')
    print()

Replace the *** in the nested loops to display two rows, each containing seven '@' symbols:
@@@@@@@
@@@@@@@
"""
# Solution: 
for row in range(2):          
    for col in range(7):      
        print('@', end='')    
    print()                   # Newline after each row


"""
3.9 (Separating Digits in an Integer) review [week4 addtional3.py]
Reimplement a script to separate a 7-10 digit integer into individual digits using // and %.
Example: Input 12345678 → Output 1 2 3 4 5 6 7 8(one in each row)
"""
# Solution: 
num = int(input("Enter a 7-10 digit integer: "))
length = len(str(num))
divisor = 10 ** (length - 1)  

while divisor >= 1:
    digit = num // divisor    # Extract leftmost digit
    print(digit)
    num %= divisor            # Remove the extracted digit
    divisor //= 10            # Move to the next lower place value



"""
3.11 (Miles Per Gallon)
Terminate when -1 is entered for gallons.
"""
#Solution:
total_miles = 0.0
total_gallons = 0.0

while True:
    gallons = float(input("Enter gallons used (-1 to end): "))
    if gallons == -1:
        break
    else:
        miles = float(input("Enter miles driven: "))
        mpg = miles / gallons
        print(f"The miles/gallon for this tank was {mpg:.6f}")
        total_miles += miles
        total_gallons += gallons

print(f"The overall average miles/gallon was {total_miles/total_gallons:.6f}")


"""
3.12 (Palindromes)
Determine if a 5-digit integer is a palindrome (reads same backward).
"""
# Solution 1 take it as string: 
num_str = input("Enter a 5-digit number: ")

if  (num_str[0] == num_str[4] and num_str[1] == num_str[3]):
    print(f"{num_str} is a Palindrome.") 
else:
    print(f"{num_str} is Not a palindrome.")

#Solution 2 take it as integer:
num = int(input('Enter a 5-digit number: '))

first_two_digits = num // 1000
reversed_last_two_digits = num % 10 *10 + num // 10 % 10 

if first_two_digits == reversed_last_two_digits:
    print(f"{num} is a Palindrome.") 
else:
    print(f"{num} is Not a palindrome.")



"""
3.14 (Approximating π)***** important 在下一轮开启前赋值 previous_pi = pi_approximation
Compute π using the series: π = 4/1 - 4/3 + 4/5 - 4/7 + ...
You can just approximate to 3.14 and 3.141
at what iteration of the loop you see 3.14 twice in a row,
And 3.141
"""
#Solution:

def pi_approximation(precision, max_iterations):
    import math
    pi_approximation = 0
    previous_pi = 0
    target = round(math.pi,precision)

    for i in range(max_iterations):
        pi_approximation += 4 * (-1)**i / (2*i + 1)
        if round(pi_approximation, precision) == target and round(previous_pi, precision) == target:
            print(f"{round(math.pi, precision)} found at iteration {i} and {i+1}.")
            return i
        previous_pi = pi_approximation
        
    else:
        print(f"{round(math.pi, precision)} not found in {max_iterations} iterations")
        return None

pi_approximation(2, 1000)
pi_approximation(3,3000)
        

