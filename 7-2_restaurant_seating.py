limit = 8
num_people = input("How many are in your group?\n>> ")
num_people = int(num_people)

if num_people > limit:
    print("Please wait for a table.")
else:
    print("A table is ready.")
