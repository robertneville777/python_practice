favorite_places = {'mom':['beach','city'],
    'dad':['mountains','country side','gun range'],
    'rio':['desert','mx track']
    }

for key,val in favorite_places.items():
    print(key.title() + "'s favorite places are: ")
    for places in val:
        print(places.title())
    print("")
