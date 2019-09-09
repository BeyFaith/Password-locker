class Info:

    '''
    class that generates new instances of login credentials.

    '''

    info_list = []

    def __init__(self,face_bookp,email_book_p):

        '''
        define properties for my class.

        '''
        self.face_bookp = face_bookp
        self.email_p = email_book_p

    def  save_info(self):

        '''
        function to save credentials

        '''
        Info .info_list.append(self)

    def delete_info(self):

        '''
        function added to delete credentials
        '''

        Info.info_list.remove(self)

    @classmethod
    def display_info(cls):

        '''
        class method that works through ut the whole class to display info.
        '''

        return cls.info_list
