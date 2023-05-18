from flask import Flask, jsonify, request
from dbconnect import get_mysql_connection

app = Flask(__name__)
db_connection = get_mysql_connection()

# get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        cursor.close()
        response = {'error': False, 'message': 'success', 'count': len(rows), 'users': rows}
        return jsonify(response), 200
    except Exception as e:
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

# get user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE id=%s', (id,))
        row = cursor.fetchone()
        cursor.close()
        if not row:
            response = {'error': True, 'message': 'User not found'}
            return jsonify(response), 404
        response = {'error': False, 'message': 'success', 'user': row}
        return jsonify(response), 200
    except Exception as e:
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

# create new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        if not data or not all(key in data for key in ['Username', 'Email', 'Password', 'Gender', 'BirthDate', 'Height', 'Weight', 'FatNeed', 'ProteinNeed', 'CaloryNeed', 'FiberNeed', 'CarbohidrateNeed']):
            return 'Missing fields', 400
        cursor = db_connection.cursor()
        query = 'INSERT INTO users (Username, Email, Password, Gender, BirthDate, Height, Weight, FatNeed, ProteinNeed, CaloryNeed, FiberNeed, CarbohidrateNeed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        values = (data['Username'], data['Email'], data['Password'], data['Gender'], data['BirthDate'], data['Height'], data['Weight'], data['FatNeed'], data['ProteinNeed'], data['CaloryNeed'], data['FiberNeed'], data['CarbohidrateNeed'])
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()
        response = {'error': False, 'message': 'User created'}
        return jsonify(response), 201
    except Exception as e:
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

# update existing user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.json
        if not data:
            return 'Missing fields', 400
        cursor = db_connection.cursor()
        query = 'UPDATE users SET '
        values = []
        for key in data:
            query += key + '=%s, '
            values.append(data[key])
        query = query[:-2]   # remove last comma and space
        query += ' WHERE id=%s'
        values.append(id)
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()
        response = {'error': False, 'message': 'User updated'}
        return jsonify(response), 200
    except Exception as e:
        db_connection.rollback()
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

# delete user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        cursor = db_connection.cursor()
        cursor.execute('DELETE FROM users WHERE id=%s', (id,))
        db_connection.commit()
        cursor.close()
        response = {'error': False, 'message': 'User deleted'}
        return jsonify(response), 200
    except Exception as e:
        db_connection.rollback()
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500


# get all intake users
@app.route('/intake_users', methods=['GET'])
def get_intake_users():
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM intake_users')
        rows = cursor.fetchall()
        cursor.close()
        response = {'error': False, 'message': 'success', 'count': len(rows), 'intake_users': rows}
        return jsonify(response), 200
    except Exception as e:
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

# get intake user by id
@app.route('/intake_users/<int:id>', methods=['GET'])
def get_intake_user(id):
    try:
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM intake_users WHERE id=%s', (id,))
        row = cursor.fetchone()
        cursor.close()
        if not row:
            response = {'error': True, 'message': 'Intake User not found'}
            return jsonify(response), 404
        response = {'error': False, 'message': 'success', 'intake_user': row}
        return jsonify(response), 200
    except Exception as e:
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

# create new intake user
@app.route('/intake_users', methods=['POST'])
def create_intake_user():
    try:
        data = request.json
        if not data or not all(key in data for key in ['user_id', 'HealthStatus', 'FatIntake', 'CaloryIntake', 'FiberIntake', 'CarbohidrateIntake', 'Feedback']):
            response = {'error': True, 'message': 'Missing fields'}
            return jsonify(response), 400
        cursor = db_connection.cursor()
        query = 'INSERT INTO intake_users (user_id, HealthStatus, FatIntake, CaloryIntake, FiberIntake, CarbohidrateIntake, Feedback) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        values = (data['user_id'], data['HealthStatus'], data['FatIntake'], data['CaloryIntake'], data['FiberIntake'], data['CarbohidrateIntake'], data['Feedback'])
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()
        response = {'error': False, 'message': 'Intake user created'}
        return jsonify(response), 201
    except Exception as e:
        db_connection.rollback()
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

# update existing intake user
@app.route('/intake_users/<int:id>', methods=['PUT'])
def update_intake_user(id):
    try:
        data = request.json
        if not data:
            response = {'error': True, 'message': 'Missing fields'}
            return jsonify(response), 400
        cursor = db_connection.cursor()
        query = 'UPDATE intake_users SET '
        values = []
        for key in data:
            query += key + '=%s, '
            values.append(data[key])
        query = query[:-2]   # remove last comma and space
        query += ' WHERE id=%s'
        values.append(id)
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()
        response = {'error': False, 'message': 'Intake user updated'}
        return jsonify(response), 200
    except Exception as e:
        db_connection.rollback()
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

# delete intake user
@app.route('/intake_users/<int:id>', methods=['DELETE'])
def delete_intake_user(id):
    try:
        cursor = db_connection.cursor()
        cursor.execute('DELETE FROM intake_users WHERE id=%s', (id,))
        db_connection.commit()
        cursor.close()
        response = {'error': False, 'message': 'Intake user deleted'}
        return jsonify(response), 200
    except Exception as e:
        db_connection.rollback()
        response = {'error': True, 'message': str(e)}
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
