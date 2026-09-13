# Pythong number guessing game
import random

lowest_number = 1
highest_number = 100
answer  = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print("If you want to quit the game, type 'exit'.")
print(f"I'm thinking of a number between {lowest_number} and {highest_number}. Can you guess what it is?")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print(f"Please guess a number between {lowest_number} and {highest_number}.")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {answer} in {guesses} attempts.")
            is_running = False
    elif guess.lower() == "exit":
        print("Thanks for playing! Goodbye.")
        is_running = False
    
    else :
        print("Please enter a valid number.")
        print(f"Please guess a number between {lowest_number} and {highest_number}.")

     