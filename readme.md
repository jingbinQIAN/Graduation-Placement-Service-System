# The Graduation Placement Service Instructions

### libraries that are used in this system

```py
pip install flask pymysql flask_sqlalchemy flask_session faker werkzeug os
```

### Tips to run our main program:
1. We used xampp to establish a virtual database.</br>
    And this database is local service and the service is on 127.0.0.1 (local host). <br>
    If you use your remote service, please modify the SQLALCHEMY_DATABASE_URI in "/app/config/secure.py" file: <br>
    "root@127.0.0.1" change to your own address.<br>
    "GPSdatabase" is the database's name (strongly recommend to use "gpsdatabase.sql" to load our database).<br>
2. Load the database:<br>
    Open phpMyAdmin webpage<br>
    Create a database named "gpsdatabase"<br>
    In the toolbar, click "import" and load the "gpsdatabase.sql" file.
3. Run the file "**teamwork.py**" to run this system
4. Open the website "http://127.0.0.1:5000/user/login" to open the system's homepage.

### Explanation of the files:
1. In the root folder: <br>
    "teamwork.py" is the main function to run our project. <br>
    If you use PyCharm editor, open this file and trust the project. Then the whole project can be open and edited. <br>
    "gpsdatabase.sql" is the file for you to load our database. <br>
2. In the folder "./app", there are the sub functions (codes) of our project. <br>
    "/app/models": the entities (classes) are there. <br>
    "/app/controller": the functions to implement all the use cases there. <br>
    "/app/templates": the html files for creating and decoration webpages. <br>
    "/app/config": the place for you to change your own database. <br>
    "/app/static": the place to store the website images. <br>
    "/app/offerImages": the sample offer images for you to test the system (Provide Offer Information). <br>
    "/app/_pycache": the cache of python program, please ignore it. <br>
3. In the folder "./test", there are the test codes for unit testing, LoadRunner testing. <br>
    "/test/test_login.py": the unit test for login. <br>
    "/test/unittestResult": the result of the login test. <br>
    "/test/UICerSearchGPA": the LoadRunner Script for UICer search admission requirement by GPA. 
4. The folders ".idea", "__pycache", "flask_session": <br>
    Please ignore them, they are automatically generate by python. <br>
    **If there is an error when using the website:** <br>
    "TypeError: '<' not supported between instances of 'NoneType' and 'float' " <br>
    please try to delete all the files in "flask_session" and run again. <br>
    It is the mistake of flask_session package, not our programs' bug.


### THE END. Thanks for reading this instruction.
