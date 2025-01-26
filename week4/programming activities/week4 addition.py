"""
Write in pseudocode and then in Python a program that simulates a guessing game. 
The program should randomly choose a number between 1 and 100. 
The user must guess the number, and the program will tell the user if their guess is too high, too low, or correct. 
The game should continue until the user guesses the correct number or chooses to quit. 
The program should also keep track of how many guesses the user made.
"""
import random
# Generate random target number
target_number = random.randint(1,100)
guess_count = 0
print('''
      It is a guessing game and I have generated a random integer between 1 and 100.
Try to guess it or type 'quit' to exit at any time.
''')
while True:
    guest_input = input('Enter your guess:')
     # Check if the user wants to quit
    if guest_input == 'quit':
        print('Thanks for playing.')
        break
    else:
        guest_input = int(guest_input)
        guess_count += 1
        # Check if the guess matches the target
        if guest_input == target_number:
            print(f'Congratulations! You guessed the number in {guess_count} tries.')
            break
        elif guest_input < target_number:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")
