# Django Project for financepeer.com

Json file processing using Django/Python/JavaScript/PostgreSQL 

can be viewd at below url 

### https://financepeer2022.herokuapp.com
and the repository can be downloaded from gitbub at https://github.com/DayakarMalgari/FinancePeer

## 1. Installation guidelines.
### a). after downloading the repository, in settings.py file change the below data with your values.
 'USER': 

 'PASSWORD':

 'HOST': 'localhost',

 'PORT': '5432',

 'database':

 
### b). Install all packages from the requirements.txt file using pip and run below 3 commands at command prompt from the folder where you have manage.py file and where you have access to python interpreter.
     
 python manage.py makemigrations

 python manage.py migrate

 python manage.py runserver

 then use localhost:8000 or 127.0.0.1:8000 to access the application

## 2. Application usage details.
### Home page
  click either the Admin button to use admin panel or User button to use the application
### Login page / sign-up page
  first time users should click the sign-up button to go to sign-up page to register with username, emailid and password.
  you can mention email-id at username as well if you wish.
   Once registed, it redirects back to login page to login with newly created credentials.
### User Data Search Page has 5 tabs. 1. File Upload 2. View All Data 3. Select User Data 4. financepeer 5. logout 
### File Upload page
 enter the emailid which you used to login, choose the file / json file to upload and then click upload button.
 once done you will get the confirmation. You can load the file into database only once as there is unique constraint on id.
 You need to delete all data before loading second time
### View all Data page
 will just display all user data from the database in one shot, you just need to click the tab thats all.
 Search fields are also active, however, you will be redirected User Data Search Page if you enter proper criteria.
### User Data Search Page
  This is the main page which has the full functionality. In the search options,

  a. ID Field has the top priority, if you enter any number greater than 0 in this field it will activate and, 
  will ignore the rest 2 search criterion fields even if you enter any valid values. This criterion will fetch only one record.

  b. UserID field has the second priority and will also take values greater than 0. This will get activated only if ID field is empty or 0. This criterion will fetch all records under that user.

  c. Title field has the last priority, and will activate only if ID and UserID fields are empty or 0's.
  You can use this field in 2 ways; one with checkbox checked for full title search, which will fetch only one record assuming title is unique.
  and second way is with checkbox unchecked, and in this case will fetch multiple users records whose title field contain at least one word from
  the words in the search box. For example.

  placeat quia et porro iste                                - will fetch 18 records if unchecked, and 1 record if checked

  quaerat velit veniam amet cupiditate aut numquam ut sequi - will fetch 24 records if unchecked, and 1 record if checked
### financepeer 
  just a link to financepeer.com
### Logout doesn't have a page
  but once clicked, asks for confirmation if you really want to log out or not. 
  If you click cancel, you will remain in the same page, and will log you out if replied ok to the confirmation.


## 3. Unit testing and alert message details:
Below are the variables used and the criteria when the message gets triggered.

 a. jsonDocsnotfound       - when you search on search page and there are no records to display from the database

 b. criterianotentered     - when you try to search for user data without entering any criteria or if you enter negative values in ID and UserID search fields

 c. toomanykeys            - SQLITE Specific, when you enter too many key words in title search box, like more than 10 words, Sqlite database will fail to serve.

 d. unknownerror           - any error not caught by other error messages mentioned here.

 e. Integrity              - you can load a json file only once, as there is a unique constraint on ID field. Multiple uploads will not populate fields in RDBMS table. 

 f. logout confirmation    - when you log out from any page, it asks for your confirmation

 g. filenotselected        - when you click upload button without selecting any file

 h. emailnotentered        - when you click upload button without entering your emailid

 i. saved                  - when file uploaded to media folder and also loaded into the postgreSQL database

 j. emaiidnotfound         - when you try to upload a file with emailid other than what you used to login

 k. fullnamenotentered     - when you do not enter username while sign-up, it gives a message

 l. passwordnotentered     - when you do not enter password and click upload

 m. emailfound             - when you try to sign-up twice with same email-id, or with any registered email-id.

 n. Invalidcredent         - Error from django authentication system about invalid credentials

 o. emaiidnotfound         - when you try to sign-in with unregistered email-id

 p. InvalidData            - when django fails to validate form data

 q. loggedout              - when you log out, after replying ok to log out confirmation

 r. signup                 - congratulating you on successful sign-up
 
 s. notrighttype           - if you try to upload any file other than json this would get triggered
 
 t. notrightformat         - if the uploaded json file is not in the right format this would get triggered. it expects 4 fields, of right types and names.
 
 u. validation             -  if negative values are used to search users in search ID and UserID boxes, this would get triggered.

 
