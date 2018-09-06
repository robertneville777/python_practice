from user import User
from privilege import Privileges

class Admin(User):
    """ Admin info """

    def __init__(self,name_first,name_last,age_in,fav_char_in):
        """ Initialize attributes of the parent class """
        super().__init__(name_first,name_last,age_in,fav_char_in)
        self.rights = Privileges()
