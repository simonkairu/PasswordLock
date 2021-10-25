#!/usr/bin/env python3.9
from user import User, Credentials

def create_new_user(username,password):
    '''
    This will create a function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    This will  create a function to save a new user
    '''
    user.save_user()
def display_user():
    """
    This will create a function that will display existing user 
    """
    return User.display_user()
def login_user(username,password):
    """
    It creates a function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    
    This function will find a credential by account name and then return credentials related to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)


def passlocker():
    print("Welcome to your Accounts Password Store...\n  To proceed Kindly select one.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('.' * 50)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password try again")
        save_user(create_new_user(username,password))
        print("."*50)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("."*50)
    elif short_code == "li":
        print("."*50)
        print("Enter your User name and your Password to log in:")
        print('.' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To PassWordLocker Manager")  
            print('\n')
    while True:
        print("Use these short codes:\n CN - Create a new credential  DC - Display Credentials  FC - Find a credential GP - Generate A randomn password DL - Delete credential EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cn":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of accounts: ")
                 
                print('.' * 50)
                print('_'* 50)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 50)
                print('.' * 50)
            else:
                print("You don't have saved credentials ..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('.' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('.' * 50)
            else:
                print(" Credential does not exist")
                print('\n')
        elif short_code == "dl":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your  credentials for : {search_credential.account}  deleted successfully!!!")
                print('\n')
            else:
                print("credential to be deleted does not exist")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} Has been generated succesfull.")
        elif short_code == 'ex':
            print("Thank You for using passwordlocker.. See again!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Invalid input try again")

if __name__ == '__main__':
    passlocker()