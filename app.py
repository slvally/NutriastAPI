from flask import Flask, jsonify, request
from dbconnect import get_mysql_connection

app = Flask(__name__)

db_connection = get_mysql_connection()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users',  methods=['GET'])
def get_users():
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM users")
    result = cur.fetchall()
    return jsonify(result)

@app.route('/users',  methods=['POST'])
def add_users():
    try:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cur = db_connection.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
        db_connection.commit()

        response = {
            "message": "User created successfully"
        }
        return jsonify(response), 201
    except Exception as e:
        error_message = str(e)
        response = {
            "message": "Error creating user",
            "error": error_message
        }
        return jsonify(response), 500

# example to return specified attribute
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
    result = cur.fetchone()
    if result is None:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(result[2])

if __name__ == '__main__':
    app.run(debug=True)