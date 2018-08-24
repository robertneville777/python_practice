class Restaurant():
    """ Simple model for a restaurant."""

    def __init__(self,restaurant_name,cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type  = cuisine_type

    def describe_restaurant(self):
        """Display restaurant attributes."""
        print(self.restaurant_name.title() + " serves "
            + self.cuisine_type + ".")

    def open_restaurant(self):
        """Report that restaurant is open."""
        print(self.restaurant_name.title() + " is open.")

albert_tacos = Restaurant('albert tacos','tacos')
burger_king = Restaurant('burger king','burgers')
subway = Restaurant('subway','sandwiches')

albert_tacos.describe_restaurant()
burger_king.describe_restaurant()
subway.describe_restaurant()
