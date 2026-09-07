# conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of two values based on a condition
#                           X if condition else Y

num = 7
a = 4210
b = 577
age = 25
temperature = 30
user_role = "user"

# print("Positive" if num > 0 else "Negative")
result = "EVEN" if num % 2 == 0 else "ODD"
max_num = a if a>b else b
min_num = a if a>b else b
Status = "Adult" if age >= 18 else "Child"
Weather = "hot" if temperature > 20 else "cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)