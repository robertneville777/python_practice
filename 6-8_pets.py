lightfoot = {'kind':'dog','owner':'ray schad'}
beatrice  = {'kind':'dog','owner':'john schad'}
lizard_boy= {'kind':'lizard','owner':'nicholas calvi'}
blastoise = {'kind':'tortoise','owner':'clint schad'}

pets = [lightfoot,beatrice,lizard_boy,blastoise]

for pet in pets:
    for key,value in pet.items():
        print(key.title() + ": " + value.title())
    print("")
