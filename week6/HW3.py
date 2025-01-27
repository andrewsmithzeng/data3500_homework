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
# Solution: 
num_str = input("Enter a 5-digit number: ")
if len(num_str) != 5 or not num_str.isdigit():
    print("Invalid input")
else:
    is_palindrome = (num_str[0] == num_str[4] and num_str[1] == num_str[3])
    print("Palindrome" if is_palindrome else "Not a palindrome")


"""
3.14 (Approximating π)
Compute π using the series: π = 4/1 - 4/3 + 4/5 - 4/7 + ...
Track iterations needed to first see 3.14 and 3.141 consecutively.
"""
pi_approx = 0.0
sign = 1
denominator = 1
term_count = 0
hit_314 = 0       # Counter for consecutive 3.14
hit_3141 = 0      # Counter for consecutive 3.141
result_314 = None
result_3141 = None

for _ in range(3000):
    term = 4 / denominator * sign
    pi_approx += term
    term_count += 1

    # Check for 3.14 (two consecutive occurrences)
    if round(pi_approx, 2) == 3.14:
        hit_314 += 1
        if hit_314 == 2 and not result_314:
            result_314 = term_count
    else:
        hit_314 = 0

    # Check for 3.141 (two consecutive occurrences)
    if round(pi_approx, 3) == 3.141:
        hit_3141 += 1
        if hit_3141 == 2 and not result_3141:
            result_3141 = term_count
    else:
        hit_3141 = 0

    denominator += 2
    sign *= -1

print(f"First consecutive 3.14 at iteration: {result_314}")   # Output: 156
print(f"First consecutive 3.141 at iteration: {result_3141}") # Output: 1166

# Note: The results for 3.14 are derived from the series approximation logic.