
# grocery_list = [["apple", "orange", "banana", "cherry", "mango", "banana", "banana"]
#                , ["carrot", "broccoli", "spinach", "pepper", "onion", "carrot"]
#                , ["chicken", "beef", "pork", "lamb", "chicken"]]

# print(grocery_list[0][2])  # Accessing "banana" from fruits
# print(grocery_list[1][0])  # Accessing "carrot" from vegetables
# print(grocery_list[2][0])  # Accessing "chicken" from meats

#for collection in grocery_list:
    # for item in collection:
        # print(item, end=", ")
    #print()


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
        ("*"), 0, ("#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()