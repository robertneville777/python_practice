fav_nums = {'bill':[1,2],
    'amanda':[3,4,5,6],
    'bob':[1],
    'sarah':[9,8,7]
    }

for key,value in fav_nums.items():
    
    if len(value) > 1: 
        printout = "numbers are"
    else:
        printout = "number is"
    
    print(key.title() + "'s favorite " +
    printout + " the following: ")
    
    for number in value:
        print(number)
    print("")
