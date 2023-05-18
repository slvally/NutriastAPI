from flask import Flask
from dbconnect import get_mysql_connection
from routes import configure_routes

app = Flask(__name__)

db_connection = get_mysql_connection()
configure_routes(app, db_connection)

if __name__ == '__main__':
    app.run(debug=True)