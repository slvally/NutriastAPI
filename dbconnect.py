import mysql.connector

def get_mysql_connection():
    app_config = {
        'MYSQL_HOST': 'localhost',
        'MYSQL_USER': 'root',
        'MYSQL_PASSWORD': '',
        'MYSQL_DB': 'nutriast'
    }
    db_connection = mysql.connector.connect(
        host=app_config['MYSQL_HOST'],
        user=app_config['MYSQL_USER'],
        password=app_config['MYSQL_PASSWORD'],
        database=app_config['MYSQL_DB']
    )
    return db_connection
