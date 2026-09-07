#Pyton weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit =="K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit =="L":
    weight = weight / 2.205
    Unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid or recognized")



