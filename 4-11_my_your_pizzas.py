my_pizzas = ['pepperoni','cheese','sausage','pineapple','ham']
friend_pizzas = my_pizzas[:]

my_pizzas.append('extra meat')
friend_pizzas.append('onions')

print('\nMy favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
