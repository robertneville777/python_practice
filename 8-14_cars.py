def make_car(manufacturer_in,model_in,**options):
    """ Build car profile """
    car_dictionary = {}
    car_dictionary['manufacturer'] = manufacturer_in
    car_dictionary['model'] = model_in
    for key,val in options.items():
        car_dictionary[key] = val

    return car_dictionary

my_car_profile = make_car('ford','ranger',year=2007,color='blue')
print(my_car_profile)
