#while loop = execute some code WHILE some condition remains true

# name = input("Enter your name: ")

# while name == "":
#  print("You didn't enter your name!")
#  name = input("Enter your name: ")

#  print(f'Hello {name}!')

# age   =int(input("Enter your age: "))    
# while age < 0:
    # print("Age can't be negative!")
    # age = int(input("Enter your age: "))

# print(f'You are {age} years old!')

# food = input("What is your favorite food? (q to quit): ")

# while not food == "q":
    # print(f'you like {food}!')
    # food = input("enter another food you like (q to quit): ")

# print("Ok, you quit the loop!")

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is an invalid number, try again!")
    num = int(input("Enter a number between 1 and 10: "))

print(f"Ok, {num} is a valid number!")
