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


    def test_save_user(self):

        '''
        test to save user.
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def tearDown(self):

        '''
        this method cleans up after eachtestcase has run.

        '''
        
        User.userlist = []
        

if __name__ == '__main__':
    unittest.main()       