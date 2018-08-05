prompt = "Enter desired vaction location (enter 'quit' to exit): "

locations = {}
active = 1

while active:
   user = input("Please enter name: ")
   location = input("Please enter desired location: ")

    # store user info in locations dictionary
   locations[user] = location

   flag = 1 
   while flag:

      keep_going = input("Does another user want to "
         "enter the poll? ['yes','no'] ")

      if keep_going == 'no':
         active = 0
         flag = 0
      elif keep_going == 'yes':
         active = 1
         flag = 0
      else:
         print("Invalid input.")

print('\n\nResults of poll:\n')

for user, location in locations.items():
    print(user.title() + ": " + location.title())
