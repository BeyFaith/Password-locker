global users_list

class User:

    """

    Class that generates new instances of user login into my aplication.

    """

    users_list = []

    def __init__(self,first_name,last_name,password):

        """
        Define properties for my object.

        """

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):

        '''
        method to save new user.
        '''

        User.users_list.append(self)

class Credential:
    
       