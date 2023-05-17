## Install Requirements
- Python 3.9.7 and pip https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe
- Add environment system variables C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\
- Check your python version using command "python --version" make sure it is Python 3.9.7

## Open Project File
- In your code editor open file "FlaskNutriastAPI"

## Install environment
- open your terminal on the file directory
- run command "virtualenv env"
- run "env\scripts\activate.bat"

## Install FLASK
- run command "pip install flask"

## Create MySQL Database
- install XAMPP 8.0.3
- start MySQL
- put file nutriast.sql in your C:\ directory
- run command "mysql -u root"
- run command "create database nutriast;"
- run command "exit"
- run command "mysql -u root -p nutriast < C:\nutriast.sql"

## Run
- run command "flask run"
- API run on http://127.0.0.1:5000