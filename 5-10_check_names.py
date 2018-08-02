current_users = ['clint','John','rio','eli','ryan']
new_users = ['Clint','john','elvis','hector','mike']

for num in range(0,len(new_users)):
    if new_users[num].lower() == current_users[num].lower():
        print('Username unavailable. Pick new username.')
    else:
        print('Username available.')
