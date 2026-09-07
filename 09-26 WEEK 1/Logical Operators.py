#Logical Operators = Evaluate multiple conditions (or, and, not)
#                   or = at least one condition must be true
#                   and = both conditions must be true
#                   not = inverts the condition (not False or not True)

#temp = 20
#is_raining = True

#if temp > 35 or temp < 0 or is_raining:
      #  print("The outdoor event is canceled")
#else:
       # print("The outdoor event is still scheduled")

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <=  0 and is_sunny:
    print("It is COLD outside")
    print("It is sunny")
elif temp < 28 and temp >0 and is_sunny:
    print("It is WARM outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is sunny")
elif temp <=  0 and  not is_sunny:
    print("It is COLD outside")
    print("It is sunny")
elif temp < 28 and temp >0 and not is_sunny:
    print("It is WARM outside")
    print("It is sunny")
