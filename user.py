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

    '''
    class that generates new instances of login credentials.

    '''

    credentials_list = []

    user_credentials_list = []

    @classmethod
    def check_user(cls,first_name,password):
        
        '''
        method to checkif user and password entered matches what is entered.
        '''
        current_user = ''
        for user in User.users_list:
            if(user.first_name ==first_name and user.password == password):
                current_user = user.first_name
            return current_user

    def __init__(self,user_name,site_name,account_name,password):

        '''
        method to definetheproperties for user object.
        '''

        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):

        '''
        function to save new created credentials.
        '''

        Credential.credentials_list.append(self)

    def generate_password(size=5, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):

        '''
        function that willgenerate a 5 character password.
        '''
        gen_pass = ''.join(random.choice(char) for x inrange(size))
        return gen_pass

    @classmethod
    def display_credentials(cls,user_name)
        '''
        method that will display credentials'list
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)

        return user_credentials_list


    @classmethod
    def find_by_site_name(cls,site_name):
        '''
        method that returns a site name that matches a credential.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential


    @classmethod
    def copy_credential(cls,site_name):
        '''
        method that copies credential's info
        '''
        find_credential = Credential.find_by_site(site_name)
        return pyperclip.copy(find_credential.password)       