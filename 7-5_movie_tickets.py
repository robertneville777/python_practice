prompt = "Please enter age: "
prompt+= '(enter "quit" to exit) >> '

flag = 1

while flag == 1:

    age = input(prompt)

    if age == 'quit':
        flag = 0
    else:
        age = int(age)
    
        if age < 3:
            print('Ticket is free')
        elif age < 12:
            print('Ticket is $10.')
        else:
            print('Ticket is $15.')
