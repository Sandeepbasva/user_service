user_service
==============

API service for user activity

Pre-requisites
------------
* Clone the git code base.
* Install required packages by pip. Use
```
$ pip install -r requirements.txt
```
to install the needed packages. Use of virtualenv is recommended to have an isolated environment for development.

Database Management
-----------------

 To create database tables use below migration commands.
```
$ python manage.py makemigrations 
```

Run 
```
$ python manage.py migrate 
```
to apply the migrations.


Deployment
----------

* Use pythonanywhere for free hosting.

