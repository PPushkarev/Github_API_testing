

#  Python POM API Framework for GitHub
## There are 2 Test cases to create, check and delete repository on Github using API 
	
### Test test_create_repository

* Create public original name repository on Github, 
* then checked it creation from list of all repositories in  this account,
* If repository is appear in this list, test is passed

### Test test delete_repository

* Create public original name repository on Github, 
* then checked it creation from list of all repositories on this account and,
* then delete it 
* If repository had removed from list of repositories, test is passed


### The tech stack used in this project are:

```
Python as the programming language for writing test code-
VSCode as the preferred IDE for writing python code.
PIP3 as the build tool
Requst 
python-dotenv
random
```
    

### Features:
- All tests are independent from each other

- Using random names for each test to create original repository name from .env

- Using time sleep in delete_repository test, because of postpone delete repository process by Github Backend.  So need a wait.

- Sample of TOKEN in .env valid until 11/10/2024 

### Design pattern 
  ```
Page object model (POM)
  ```

### Structure of project:

- test_api.py - contents scripts of all tests 

- requirements.txt -is a file that contains a list of packages or libraries needed to work on a project that can all be installed with the file.

- .env- configuration file with personal information about account name, token, name repository that going to create
- README.md - information for installing and using this framework 
- 
Directory Endpoints: 

- create_endpoint.py - one function for creation repository using method POST

- get_endpoint.py-  two function for checking creation and removing repositories using method GET

- delete_endpoint.py- one function for delete repository using method DELETE




## What to need to do run all tests

### Have personal account on Github 
	Overwise pass all registration steps to get your personal account on Github

### Get Bearer Token 
 ```
In the upper right corner of any page on GitHub, click your profile photo
then click Settings. 
In the left sidebar, click Developer settings. 
In the left sidebar, under Personal access tokens, 
click Fine-grained tokens. 
Click Generate new token
 ```
### Transfer information you get using this sample into file .env

  ```
USER_NAME=<NAME OF YOU ACCOUNT IN GITHUB>
REPO_NAME=<FUTURE REPOSITORY NAME IN GITHUB>
TOKEN = Bearer <TOKEN THAT YOU GET FROM BEFORE >
  ```
### Create virtual environment 
  ```
python -m venv venv 
  ```
### Activate virtual environment pip
  ```
.\venv\scripts\activate  
  ```
### Install all packages and prepare your environment 




Install all packages in your IDE,  type in  Terminal command:
  ```
pip install -r requirements.txt
  ```


### Run test 
In order to run all tests type this in Terminal IDE  

  ```
  pytest -v   
  ```


