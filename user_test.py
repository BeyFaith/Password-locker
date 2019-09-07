import unittest # Import the unittest module

from user import User # import the user class

class TestUser(unittest.TestCase):

    '''

    Test class that will define test cases for the user class behavior.

    '''
    def setUp(self):

        self.new_user = User("Bey","Faith","fryumugabe@gmail.com","hello123")