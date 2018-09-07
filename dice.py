from random import randint

class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        roll_result = randint(1,self.sides)
        print('You rolled a ' + str(roll_result) + '.')

    def set_num_sides(self,num_sides):
        self.sides = num_sides
