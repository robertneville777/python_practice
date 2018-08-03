rivers = {'nile':'egypt','kern river':'America','mississippi':'America'}

print("")

for key_river, value_river in rivers.items():
    print("The " + key_river.title() + " runs through " 
    + value_river.title() + ".\n")

print("The rivers in the dictionary are:")
for river in rivers.keys():
    print(river.title())
print("")

print("The countries in the dictionary are:")
for country in set(rivers.values()):
    print(country.title())
print("")
