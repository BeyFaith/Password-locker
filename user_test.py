import unittest # Import the unittest module

from user import User # import the user class

class TestUser(unittest.TestCase):

    '''

    Test class that will define test cases for the user class behavior.

    '''
    def setUp(self):

        self.new_user = User("Bey","Faith","fryumugabe@gmail.com","hello")

    def test_1(self):

        '''
        test case  to test the initilization of the object.
        '''

        self.assertEqual(self.new_user.first_name,"Bey")
        self.assertEqual(self.new_user.last_name,"Faith")
        self.assertEqual(self.new_user.email,"fryumugabe@gmail.com")
        self.assertEqual(self.new_user.password,"hello")


if__name__ == '__main__':
    unittest.main()        