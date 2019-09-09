#!/usr/bin/env python3.6

from user import User
from credentials import Info

def create_account(first_name,last-name,email):
    '''
    function to create new account user
    '''

    new_user = user(first_name,last_name,email)
    return new_user

def create_credentials(facebookp,emailp):
    '''
    function to create new credential.
    '''

    new_cred = Info(facebookp,emailp)
    return new_cred

def save_account(user):
    
    '''
    function to save user
    '''

    user.save_user()

def save_credentials(credentials):

    '''
    function to save credentials.
    '''

    credentials.save_info()

def display_users():
    '''
    function to display users
    '''
    return User.display_users()

def  display_creds():
    '''
    function to display credentials
    '''
    return Info.display_info()  


def main():
    print("Hello welcome to your password-locker app.")
    print('/n')    
    
    while True:
        print("-" * 156)
        print(''' Use the following short codes: cc-create new account, ex-exit password locker,dac-display accounts,gs-generate passwords''' )
        print(" ")
        print("  Type in a short code!")
        print(" ")

        short_code = input().lowe()
        if short_code =='cc':
            print(" ")
            print("-" * 156)
            print("      Createa new account")
            print(" ")
            print(" ")
            print("what is your first name?")
            print(" ")
            first_name = input()
            print("What is your last name?")
            print(" ")
            last_name = input()
            print("what is your email address?")
            print(" ")
            email = input()
            print("what is your facebook password?")
            print(" ")
            face_bookp = input()
            print("what is your email password?")
            print(" ")
            emailp = input()
            save_account(create_account(first_name,last_name,email))
            print('/n')
            save_credentials(create_credentials(face_bookp,emailp))
            print('\n')
            print("-" *156)
            print(f"New Account {first_name} {last_name} {face_bookp} has been created")
            print('\n')
        
        elif short_code == 'dac':

            if display_users():
                print(" ")
                print("The user name")
                print(" ")
                print('\n')
                for user in display_users():
                    print(f"{user.first_name} {user.last_name}")
                for credentials in display_creds():
                    print(f"{face_bookp}")
                    print(" ")

            else:
                print('\n')    
                print("-" * 156)
                print(" ")
                print("  Please create an account")
                print("   you have not created an account with password-locker yet!!")
                print(" ")


        elif short_code == 'gs':
            print(" ")
            print(" ")
            print("To generate password add in your first name and facebook below.")
            print(" ")
            list_of_inputs = [cfor c in input()]
            list_of_inputs.reverse()
            print(list_of_inputs)


        elif short-code == "ex":
            print("-" * 156)
            print(" ")
            print("Thanks for usingpassword-locker!")
            print("Bye!!!")
            print(" ")
            print("-" * 156)
            break

        else:
            print("-" * 156)
            print(" ")
            print("  retry!")
            print(" ")
            print("   Please select one of the available options.")
            print(" ")

if __name__ == '__main__':
    main()           
