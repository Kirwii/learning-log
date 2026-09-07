# Python Calculator

operator = input ("Enter an operator (+ - * / ^): ")
num1 = float(input ("Enter the 1st number: "))
num2 = float(input ("Enter the 2nd number: "))

if operator == "+":
    Result=num1 + num2
    print(round(Result, 3))
elif operator == "-":
    Result=num1 - num2
    print(round(Result, 3))
elif operator == "*":
    Result=num1 * num2
    print(round(Result, 3))
elif operator == "/":
    Result=num1 / num2
    print(round(Result, 3))
elif operator == "^":
    Result=num1 ** num2
    print(round(Result, 3))
else:
    print(f"{operator} is not a valid operator")


