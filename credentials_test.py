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



if __name__ == '__main__':
    unittest.main()     