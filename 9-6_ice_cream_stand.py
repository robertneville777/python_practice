class Restaurant():
    """ Simple model for a restaurant."""

    def __init__(self,restaurant_name,cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type  = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display restaurant attributes."""
        print(self.restaurant_name.title() + " serves "
            + self.cuisine_type + ".")

    def open_restaurant(self):
        """Report that restaurant is open."""
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self,num):
        """ Set number of customers served"""
        self.number_served = num

    def increment_number_served(self,inc_num):
        """ Increment number of customers served"""
        self.number_served += inc_num

class IceCreamStand(Restaurant):
    """ Simple model for an ice cream stand """
    
    def __init__(self,restaurant_name,cuisine_type):
        """ Initialize attributes of the parent class."""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def list_flavors(self):
        """ List all flavors """
        for flavor in self.flavors:
            print('\t' + flavor)
        
shavedIce = IceCreamStand('shaved ice','ice cream')
shavedIce.list_flavors()
shavedIce.flavors = ['vanilla','strawberry','chocolate','mint']
shavedIce.list_flavors()
