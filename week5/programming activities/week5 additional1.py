"""
Write a Python program that simulates a simple ATM machine. 
The program should ask the user for their account balance 
and then offer them the following options in a loop:

Check Balance
Deposit Money
Withdraw Money
Quit
If the user selects "Check Balance," display their current balance. 
If they select "Deposit Money," ask how much they want to deposit and update the balance accordingly. 
If they select "Withdraw Money," ask how much they want to withdraw 
and update the balance if they have sufficient funds. If they select "Quit," exit the program. 
Make sure to use nested if statements for handling these options.

"""
balance = float(input("Enter your account balance: "))
while True:
    print("Options:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Quit")
    option = int(input("Enter your choice: "))
    if option == 1:
        print(f"Current balance: ${balance}")
    elif option == 2:
        deposit = float(input("Enter the amount you want to deposit: "))
        balance += deposit
        print(f"New balance: ${balance}")
    elif option == 3:
        withdraw = float(input("Enter the amount you want to withdraw: "))
        if withdraw > balance:
            print("Insufficient funds.")
        else:
            balance -= withdraw
            print(f"New balance: ${balance}")
    elif option == 4:
        break
    else:
        print("Invalid option. Please try again.")