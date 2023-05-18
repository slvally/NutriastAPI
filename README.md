# Readme

## Project Description
### Title:
NutriAst App
### Description:
Our project scope includes developing a mobile app that enables users to input their daily food and beverage intake, comparing their nutrient intake to daily nutritional requirements using a dataset containing nutritional information for various foods. The app provides positive feedback if the intake meets daily nutritional needs and offers suggestions if it is insufficient or excessive. Additionally, the app has a weekly health condition survey feature to monitor users' health and provide tailored advice. The system stores users' historical data and uses machine learning to make predictions about future eating patterns.
### Team and JobDesk:
The project is divided into three teams that collaborate to create an ML-based prediction application. The ML team creates a model in Python, the CC team creates APIs in Python and JavaScript for database and prediction purposes, and the MD team develops the front-end and builds a mobile application.

## System Detail
### Architecture or Workflow
The workflow of the project architecture:
- The ML team creates a dataset using Python and creates a prediction model.
- The CC team creates APIs using Python and JavaScript to communicate with the database and prediction model.
- The CC team implements APIs and the database into the cloud system, such as a virtual machine or app engine.
- The MD team works on the front-end and mobile application, fetching data from the API through the communication of GET, POST, UPDATE, and DELETE methods.
- The user inputs data such as age, height, weight into the form available in the mobile application.
- The form data is sent via the POST method to the API endpoint created by the CC team.
- The request is processed using the app prediction code built by the ML team and returns the predicted value.
- The predicted value is returned via the API endpoint to the MD team.
- The front-end application displays the predicted value on the user's screen.

### Infrastructure
Cloud such as: Cloud VM's and App Engine with CloudSQL database and also bucket cloud storage
Mobile App:
Machine Learning:

### Tools
Languages: Python for making API and build machine learning models
VSCode as IDE
Google Cloud Platform: Vm's and App Engine, CloudSQL DB, Bucket Storage
...

### Database
- Table users:
-> id (primary)
-> Username (varchar[255], not null)
-> Email (varchar[255], not null)
-> Password (varchar[255], not null)
-> Gender (varchar[255], not null)
-> BirthDate (date, not null)
-> Height (int[11], not null)
-> Weight (int[11], not null)
-> FatNeed (int[11], not null)
-> ProteinNeed (int[11], not null)
-> CaloryNeed (int[11], not null)
-> FibreNeed (int[11], not null)
-> CarbohidrateNeed (int[11], not null)
- Intake users:
-> id (primary)
-> user_id (ForeignKey to users)
-> HealthStatus (char[16])
-> FatIntake (int[11])
-> CaloryIntake (int[11])
-> FiberIntake (int[11])
-> CarbohidrateIntake (int[11])
-> Feedback (varchar[1024])

## Instalation (Still Working On)
### Install Requirements
- Python 3.9.7 and pip https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
- Add environment system variables C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\
- Check your python version using command "python --version" make sure it is Python 3.9.7
### Open Project File
- In your code editor open file "FlaskNutriastAPI"
### Install environment
- open your terminal on the file directory
- run command "virtualenv env"
- run "env\scripts\activate.bat"
### Install FLASK
- run command "pip install flask"
### Create MySQL Database
- install XAMPP 8.0.3
- start MySQL
- put file nutriast.sql in your C:\ directory
- run command "mysql -u root"
- run command "create database nutriast;"
- run command "exit"
- run command "mysql -u root -p nutriast < C:\nutriast.sql"
### Run
- run command "flask run"
- API run on http://127.0.0.1:5000