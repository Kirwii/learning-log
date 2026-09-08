# nested loop = A loop inside another loop. 
# The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"
#               outer loop:
#                    inner loop:

rows = int(input("Enter the # of rows? "))
columns = int(input("Enter the # of columns? "))
symbol = input("Enter a symbol to use? ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()  # print a new line after the inner loop finishes