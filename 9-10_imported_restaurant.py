from restaurant import Restaurant

taco_bell = Restaurant('taco bell','tacos')
taco_bell.describe_restaurant()
taco_bell.open_restaurant()
taco_bell.set_number_served(777)
print(str(taco_bell.number_served))
taco_bell.increment_number_served(1)
print(str(taco_bell.number_served))
