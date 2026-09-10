# dictionary = a collection of {key: value} pairs
#              ordered, changeable, and does not allow duplicates

Vertebrates = {"Mammals": "Warm-blooded animals with hair or fur, and most give live birth.",
                "Birds": "Warm-blooded animals with feathers, wings, and most can fly.",
                "Reptiles": "Cold-blooded animals with scales, and most lay eggs.",
                "Amphibians": "Cold-blooded animals that can live both in water and on land.",
                "Fish": "Cold-blooded animals that live in water and have gills for breathing."}

# print(dir(Vertebrates))
# print(help(Vertebrates))
# print(Vertebrates["Mammals"])

#if  Vertebrates.get("Mammals"):
#    print(Vertebrates.get("Mammals"))
#else:
#    print("That Vertebrate does not exist.")

# Vertebrates.update({"Insects": "Cold-blooded animals with exoskeletons, three body segments, and six legs."})
# Vertebrates.pop("Mammals")
# Vertebrates.popitem() # removes the last item in the dictionary
# Vertebrates.clear() # removes all items in the dictionary

# keys = Vertebrates.keys() #

# keys = Vertebrates.keys() # returns a view object of all the keys in the dictionary
#    print(key)
#print(keys)

# values = Vertebrates.values() # returns a view object of all the values in the dictionary
#for value in Vertebrates.values():
#    print(value)

items = Vertebrates.items() # returns a view object of all the items in the dictionary (Items = [(), (), ()])
for key, value in Vertebrates.items():
    print(f"{key}: {value}")
