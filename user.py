import random
import string
import pyperclip
class User:
    """
   
    This will create a user class that will be able to generate new instances of the user

    """
    user_list = []

    def __init__(self, username, password):
        """
        
        This will create a method that will define user properties 
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        This will create a method that will save a new instance in the user list
        """
        User.user_list.append(self)
    

    @classmethod
    def display_user(cls):
        '''
        This will create a method to display users
        '''
        return cls.user_list

    def delete_user(self):
        '''
        This will create a method delet account that will delete a saved account form the list
        '''
        User.user_list.remove(self)

class Credentials():
    """
    A credentials class will be created so as to help create new objects of credentials
    """
    credentials_list = []
    @classmethod
    def verify_user(cls,username, password):
        """
        
        This will create a method to verify whether a user exists in the user list
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        """
    
       This will create a method that will define the user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        This will create a method to store new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        
        A delete credentials method will be created to delete an account credential from the credentials list
        """
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_credential(cls, account):
        """

        This will create a method that will take in an account name and returns the matching  credential of that account name

        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def copy_password(cls,account):
        """
        
        This will create a method to copy password using pyperclip
        """
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, account):
        """
        This will create a method that checks availability of credentials form the credential list and returns a boolean if the credential exists
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        """
    
        This will create a method that returns all items on the credential list

        """
        return cls.credentials_list

    def generatePassword(stringLength=8):
        """
        This will generate a random string of both number,letters and characters
        
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))