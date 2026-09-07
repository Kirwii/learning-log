
# name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

# result = len(name)
# result = name.find("t")
# result =  name.rfind("z")
# result = name.capitalize()
# result = result.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-", " ")

#print(help(str))

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

username.find(" ")

if len(username) > 12:
    print(f"Your username is too long. Please enter only 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Your username is {username}")

