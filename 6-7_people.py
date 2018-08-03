person1 = {'firstname':'ryan','lastname':'ulbricht',
    'age':26,'city':'somewhere in Michigan'}

person2 = {'firstname':'john','lastname':'schad',
    'age':20,'city':'chico'}

person3 = {'firstname':'rio','lastname':'schad',
    'age':30,'city':'san diego'}

persons_list = [person1,person2,person3]

for person in persons_list:
    for key,value in person.items():
        print(key.title() + ": " + str(value).title())
    print("")
