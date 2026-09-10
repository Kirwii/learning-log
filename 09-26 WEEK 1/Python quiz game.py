# Python quiz game

questions = ("What is the capital of France?",
            "What is 2 + 2?",
            "What is the largest ocean on Earth?",
            "What is the chemical symbol for water?",
            "What is the tallest mountain in the world?")

options = (("A) London", "B) Berlin", "C) Paris", "D) Madrid"),
            ("A) 3", "B) 4", "C) 5", "D) 6"),
            ("A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"),
            ("A) H2O", "B) CO2", "C) NaCl", "D) O2"),
            ("A) Mount Everest", "B) K2", "C) Kangchenjunga", "D) Lhotse"))

answers = ("C", "B", "D", "A", "A")
guesses  = []
score = 0
question_number = 0

print("Welcome to the quiz game!")

for questiion in questions:
    print("-------------------------")
    print(questiion)
    for option in options[question_number]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_number]} is the correct answer.")
    
    question_number += 1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")

for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"You scored {score} out of {len(questions)} questions correctly.")
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
