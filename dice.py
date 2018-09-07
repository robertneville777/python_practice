""" A class to model rolling die """

from random import randint

class Die():
    """ Simple model for rolling die """

    def __init__(self):
        """ Initialize attributes for die """
        self.sides = 6

    def roll_die(self):
        """ Roll die to produce random number between 1 and num_sides"""
        roll_result = randint(1,self.sides)
        print('You rolled a ' + str(roll_result) + '.')

    def set_num_sides(self,num_sides):
        """ Set upper-limit of random number, aka number of sides """
        self.sides = num_sides
