# for loops = execute a block of code a fixed number of times
#             You can iterate over a sequence (like a list, tuple, dictionary, set, or string)

credit_number = "1234-5678-9012-3456"

for counter in credit_number:
    print(counter)

for counter in range(1, 21):
     if counter == 13:
         print("Unlucky number")
         continue
     else:
        print (counter)

