"""
1. Find all the prime numbers (a positive integer greater than 1 that has exactly two distinct factors: 1 and itself.)
within a given range using a for loop
    why We Only Need to Check Up to the Square Root When Determining Prime Numbers

    When checking whether a number (e.g., 36) is prime, its factors always occur <in pairs>. For example:
    - 36 = 2 × 18 (factor pair: 2 and 18)
    - 36 = 3 × 12 (factor pair: 3 and 12)
    - 36 = 4 × 9 (factor pair: 4 and 9)
    - 36 = 6 × 6 (factor pair: 6 and 6)

    Key Observation:
    For any factor pair (a, b), one factor will always be less than or equal to the square root of the number, 
    and the other will be greater than or equal to the square root.

    For 36:
    - The square root is sqrt(36) = 6.
    - All factor pairs have one factor <= 6 (e.g., 2, 3, 4, or 6) and the other >= 6 (e.g., 18, 12, 9, or 6).

    Conclusion:
    If no divisors are found between 2 and sqrt(n), the number cannot have any other divisors and must be prime.
    Therefore, we only need to check numbers up to the square root to determine primality.

    This optimization significantly reduces the number of checks required, especially for larger numbers.


"""

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

#print(f"Prime numbers between {start} and {end} are:")

for prime in range(start, end+1):
    #print(prime)
    if prime >1:
        is_prime = True 

#break controls by this chunk
        for factor in range (2,int(prime ** 0.5)+1):
            #print(factor)
            if prime % factor == 0:
                is_prime = False
                break


        if is_prime:
            print(prime, end = ' ')