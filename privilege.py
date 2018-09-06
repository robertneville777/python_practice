class Privileges(): 
    """ Class for storing and displaying privileges """

    def __init__(self):
        """ Initialize privileges attribute """
        self.privileges = []

    def show_privileges(self):
        """ List admin priveleges """
        for privilege in self.privileges:
            print('\t' + privilege)
