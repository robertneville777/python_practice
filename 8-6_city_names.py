def city_country(city,country):
    """ Input city and country and return string """
    city_country_str = city.title() + ', ' + country.title()
    return city_country_str

str1 = city_country('santiago','chile')
str2 = city_country('moscow','russia')
str3 = city_country('melbourne','australia')

print('\t' + str1 + '\n\t' + str2 + '\n\t' + str3)
