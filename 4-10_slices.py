bikes = ['ktm','kawasaki','yamaha','honda','suzuki']
print('\nOriginal list:')
print(bikes)
print('\nThe first three items in the list:')
for bike in bikes[:3]:
	print(bike)

print('\nThe middle three items in the list:')
for bike in bikes[1:4]:
    print(bike)

print('\nThe last three items in the list:')
for bike in bikes[-3:]:
    print(bike)

print('\n')
