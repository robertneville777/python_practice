class User():
    """ User information """

    def __init__(self,name_first,name_last,age_in,fav_char_in):
        """ Initialize first_name and last_name attributes """
        self.first_name = name_first
        self.last_name  = name_last
        self.age        = age_in
        self.fav_char   = fav_char_in

    def describe_user(self):
        """ Display user info """
        print(self.first_name.title() + " " + self.last_name.title() + 
            "'s info: ")
        print("\t" + "Age: " + str(self.age))
        print("\t" + "Favorite Character: " + self.fav_char.title())
    def greet_user(self):
        """ Personlized message that greets the user """
        print("Yo, whaddup " + self.first_name.title() + "!")

superHaxor = User('billy','bob',12,'spiderman')
superHaxor.describe_user()
superHaxor.greet_user()

mad_scientist = User('okabe','rintaro',19,'einstein')
mad_scientist.describe_user()
mad_scientist.greet_user()

crazy_cat_gurl = User('ferris','chan',18,'cosplayers')
crazy_cat_gurl.describe_user()
crazy_cat_gurl.greet_user()
