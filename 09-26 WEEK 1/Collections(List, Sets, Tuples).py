# collection = single "variable" used to store multiple values
# list = [] # ordered, mutable, allows duplicate elements
# tuple = () # ordered, immutable, allows duplicate elements
# set = {} # unordered, mutable, no duplicate elements

# fruits = ["apple", "orange", "banana", "cherry", "mango"]
fruits = ("apple", "orange", "banana", "cherry", "mango", "banana", "banana")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

#List methods
# fruits[3] = "grape"
# fruits.append("grape")
# fruits.remove("banana")
# fruits.insert(1, "kiwi")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# Set methods
# fruits.add("grape")
# fruits.remove("banana")
# fruits.discard("orange")
# fruits.pop()
# fruits.clear()

#tuple methods
# print(fruits.index("apple"))
print(fruits.count("banana"))

print(fruits)
for fruit in fruits:
     print(fruit)