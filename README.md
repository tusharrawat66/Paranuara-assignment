Paranuara Background
====================
Paranuara is colonized and accountable to provide data of people and companies to the president of their home planet.
The Endpoints on this applications will fulfill the 3 distinguish requirements of president of Checktoporov
	a) Given a company, the Api needs to provide all the employees working in that company. 
	   In case the company doesn't have any employees adequate solution is provided for that.
	b) Given 2 people, the Api will provide the details such as (name,age,address,phone) of each individual along 
	   with list of mutual friends with brown eyes and still alive.
	c) Given 1 person, Api would provide {'name':'xyz','age':32,'favorite_fruits':["banana"], 'favorite_vegetables': ['carrot','beetroot']}.
	
	
	
	
Set Up
======
In order to set up this project, please make sure you have:
--python 3.6.5, virtualenv executable added to your environmental PATH
--mysqld and mysql 8.0.16 also added to your environmental PATH	
--You will be in the root directory 'assignmentHivery' above 'paranuara'.
--activated virtualenv 


Steps ahead:
===========
-- 'pip install -r requirements.txt' to install all the dependencies in your virtualenv.
-- manually log into mysql and create a new database of your choice by using 'create database <name>; (I named my database "paranuaraWorld")
-- make sure to change DATABASE credentials in settings.py

Important: In order to split 'fruits' and 'vegetables' from 'favouriteFood' make sure to go to python shell
		>>>import nltk 
		>>>nltk.download('all')
	  This procedure might take few seconds to minute depending upon your network and hardware.

	  

Also, you may delete the 'company.json' and 'people.json' from directory 'paranuaraApp/json_files'
and replace with your own. 	


Before starting the server make sure you hit 'python manage.py makemigrations paranuaraApp' followed by 'python manage.py migrate' in the terminal
in order to migrate changes from model.py to database tables.


'python manage.py runserver' to start server(i ran the server on default at 127.0.0.1:8000)



Api Part
========
After getting done with the above. 

First and foremost:
-------------------

uploading json data to mysql would require: 
	Method: 'GET', 'http://127.0.0.1:8000/paranuaraApp/upload_data/'

	
	
a)Given a company:
	Method: 'GET', 'http://127.0.0.1:8000/paranuaraApp/empDetails/?company=companyName'
	

b)Given 2 people:
	Method: 'POST', ' http://127.0.0.1:8000/paranuaraApp/singleDualEntity/'

	Format of the payload:
	{"names":["Deleon Orr", "Britt Alexander"]}
	
	Note: (Key 'names' is mapped in the api and should always be used as it is.)

c)Given 1 person:
	Method: 'GET', ' http://127.0.0.1:8000/paranuaraApp/singleDualEntity/?name=personName'
	

Note: I used Postman App to hit all the endpoints mentioned above.


Testing the Endpoints:
======================
In order to test all the cases do the following first:
- Stop the server if it's running using 'ctrl+c' then run these 2 commands 'python manage.py dumpdata paranuaraApp.People > people_backup.json' and 
																			'python manage.py dumpdata paranuaraApp.Company > company_backup.json'

- run 'python manage.py test'

On the console you'll notice the result of test cases written in test.py . I could have written more test cases but unfortunately time was constraint.


Feel free to get in touch if you have any queries.








