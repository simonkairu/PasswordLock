# PasswordLock

#### 24/10/2021

#### By **simon kairu**  

## Description   
A python application that allows users to create an account with a username and a password.users are also allowed to store their existing details in the app,apart from that the can also generate a password or create it manually and finally they can delete their account information that they find irrelevant.

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./userinterface.py```|Hello Welcome to your Password locker... <br>* CN ---  Create New Account * LI ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```DL```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| The application exits|   

## Installation / Setup instruction
​
#### The application requires the following installations to run
* python3.9
* pip
* pyperclip

#### Cloning
​
* Open Terminal 
​
* git clone using this  <a href = "https://github.com/simonkairu/PasswordLock.git">```link```</a>
​
* Navigate to passwordLock
​
* open with vs code

### Running the Application
* To run the application, navigate to the cloned folder and type in this commands:
​
        $ chmod +x run.py
        $ ./run.py

## Known bugs    
There are no known bugs.  

## Technologies Used
* Python3.9 

## Support and contact details
Incase of any issue or how the app can be improved <br>
Email:simonkairu14@gmail.com <br>
Cell:+254702027760

### License.
MIT Copyright (c) 2021 