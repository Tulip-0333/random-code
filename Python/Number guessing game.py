# Number guessing game in Python
import random
import time

number = random.randint(1, 100)

def guess_number():
    print("Guess a number between 1 and 100")
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100")
        guess_number()
    elif guess > number:
        print("Your guess is too high.")
        guess_number()
    elif guess < number:
        print("Your guess is too low.")
        guess_number()
    elif guess == number:
        print("You guessed the number correctly!")
        time.sleep(2)
guess_number()