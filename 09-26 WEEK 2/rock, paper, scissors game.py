import random

options = ["rock", "paper", "scissors"]
player =  None
Computer = random.choice(options)
Playing = True

while Playing:
    while player not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"Player chose: {player}")
    print(f"Computer chose: {Computer}")

    if player == Computer:
        print("It's a tie!")
    elif (player == "rock" and Computer == "scissors") or \
        (player == "paper" and Computer == "rock") or \
        (player == "scissors" and Computer == "paper"):
        print("You win!")
    else:
        print("Computer wins!") 

    if not input("Play again? (y/n): ").lower()== "y":
        Playing = False

print("Thanks for playing!")