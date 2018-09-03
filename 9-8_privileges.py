class User():
    """ User information """

    def __init__(self,name_first,name_last,age_in,fav_char_in):
        """ Initialize first_name and last_name attributes """
        self.first_name = name_first
        self.last_name  = name_last
        self.age        = age_in
        self.fav_char   = fav_char_in
        self.login_attempts = 0

    def describe_user(self):
        """ Display user info """
        print(self.first_name.title() + " " + self.last_name.title() + 
            "'s info: ")
        print("\t" + "Age: " + str(self.age))
        print("\t" + "Favorite Character: " + self.fav_char.title())

    def greet_user(self):
        """ Personlized message that greets the user """
        print("Yo, whaddup " + self.first_name.title() + "!")

    def increment_login_attempts(self):
        """ Increment the number of user's login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ Reset number of user's login attempts to 0"""
        self.login_attempts = 0

class Privileges(): 
    """ Class for storing and displaying privileges """

    def __init__(self):
        """ Initialize privileges attribute """
        self.privileges = []

    def show_privileges(self):
        """ List admin priveleges """
        for privilege in self.privileges:
            print('\t' + privilege)

class Admin(User):
    """ Admin info """

    def __init__(self,name_first,name_last,age_in,fav_char_in):
        """ Initialize attributes of the parent class """
        super().__init__(name_first,name_last,age_in,fav_char_in)
        self.rights = Privileges()


daru = Admin('daru','hashida',19,'faris')
daru.rights.show_privileges()
daru.rights.privileges = ["knows everyone's password",'can hack cern']
daru.rights.show_privileges()
