def sandwich_toppings(*toppings):
    """ Print arbitrary amount of toppings """
    print('The following toppings will be added to your sandwich:')
    for topping in toppings:
        print('\t- ' + topping)

sandwich_toppings('lettuce','tomato','jalapeno')
