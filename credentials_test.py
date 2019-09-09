import unittest
from credentials import Info

class TestInfo(unittest.TestCase):

    '''
    test class that will define tests for credentials class.

    '''
    def setUp(self):
        self.new_info= Info("bey.faith","faith.bey")

    def test_init(self):
        self.assertEqual(self.new_info.face_bookp,"bey.faith")
        self.assertEqual(self.new_info.email_p,"faith.bey")

    def test_save_info(self):

        '''
        test if user is saved
        '''
        self.new_info.save_info()
        self.assertEqual(len(Info.info_list),1)

    def tearDown(self):
        Info.info_list = []

    def test_delete_info(self):
        
        '''
        test to delete info

        '''
        self.new_info.save_info()
        test_info = Info("ismail.kabuto","kabuto.ismail")
        test_info.save_info()
        test_info.delete_info()
        self.assertEqual(len(Info.info_list),1)

if __name__ == '__main__':
    unittest.main()     