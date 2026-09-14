import random

# Welcome to the Number Guessing Game!
# Objective: Guess the randomly generated number between 1 and 100.
# Instructions:
# 1. A random number between 1 and 100 will be generated.
# 2. You must guess the number within 10 attempts.
# 3. After each guess, you'll receive feedback:
#    - 'Too low' if your guess is lower than the target.
#    - 'Too high' if your guess is higher than the target.
# 4. Enter a valid integer between 1 and 100. Non-integer inputs will prompt an error.
# 5. If you guess correctly, you win! If you exhaust all attempts, you lose.

number = random.randint(1, 100)
guessed = False

while not guessed:
    try:
        guess = int(input('Guess a number between 1 and 100: '))
        if guess == number:
            print('Congratulations! You guessed the number.')
            guessed = True
        elif guess < number:
            print('Too low. Try again.')
        else:
            print('Too high. Try again.')
    except ValueError:
        print('Please enter a valid integer.')