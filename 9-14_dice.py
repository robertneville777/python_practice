from dice import Die

print('Six-sided die rolls:')
six_sided_die = Die()
for value in range(1,11):
    six_sided_die.roll_die()

print('Ten-sided die rolls:')
ten_sided_die = Die()
ten_sided_die.set_num_sides(10)
for value in range(1,11):
    ten_sided_die.roll_die()

print('Twenty-sided die rolls:')
twenty_sided_die = Die()
twenty_sided_die.set_num_sides(20)
for value in range(1,11):
    twenty_sided_die.roll_die()
