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

superHaxor = User('billy','bob',12,'spiderman')
print(superHaxor.login_attempts)
superHaxor.increment_login_attempts()
print(superHaxor.login_attempts)
superHaxor.increment_login_attempts()
print(superHaxor.login_attempts)
superHaxor.increment_login_attempts()
print(superHaxor.login_attempts)
superHaxor.reset_login_attempts()
print(superHaxor.login_attempts)
