"""
Programming Activity 1

 1. make a variable called apple_price (set it to whatever you want)
 2. make a variable called number_purchased (set it to whatever you want)
 3. make a variable called tax and set it equal to 1.07
 4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
 5. print clearly and cleanly how many apples were purchased and the total_bill
 6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.
"""
apple_price= 3
tax = 1.07
while True: 
    number_purchased = eval(input("how many apples do you wanna purchase:"))
    total_bill = apple_price * number_purchased * tax
    if total_bill != 0:
        print(f"the apples we purchased are {number_purchased} and the total bill is {total_bill}")
        break