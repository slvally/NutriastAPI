from flask import jsonify, request

# users functions

def get_users(db_connection):
    def get():
        try:
            cursor = db_connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users')
            rows = cursor.fetchall()
            cursor.close()
            return jsonify(rows), 200
        except Exception as e:
            return str(e), 500
    return get
    
def get_user(db_connection):
    def get(id):
        try:
            cursor = db_connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users WHERE id=%s', (id,))
            row = cursor.fetchone()
            cursor.close()
            if not row:
                return 'User not found', 404
            return jsonify(row), 200
        except Exception as e:
            return str(e), 500
    return get
    
def create_user(db_connection):
    def post():
        try:
            data = request.json
            if not data or not all(key in data for key in ['Username', 'Email', 'Password', 'Gender', 'BirthDate', 'Height', 'Weight', 'FatNeed', 'ProteinNeed', 'CaloryNeed', 'FibreNeed', 'CarbohidrateNeed']):
                return 'Missing fields', 400
            cursor = db_connection.cursor()
            query = 'INSERT INTO users (Username, Email, Password, Gender, BirthDate, Height, Weight, FatNeed, ProteinNeed, CaloryNeed, FibreNeed, CarbohidrateNeed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = (data['Username'], data['Email'], data['Password'], data['Gender'], data['BirthDate'], data['Height'], data['Weight'], data['FatNeed'], data['ProteinNeed'], data['CaloryNeed'], data['FibreNeed'], data['CarbohidrateNeed'])
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            return 'User created', 201
        except Exception as e:
            db_connection.rollback()
            return str(e), 500
    return post

    
def update_user(db_connection):
    def put(id):
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
            return 'User updated', 200
        except Exception as e:
            db_connection.rollback()
            return str(e), 500
    return put
    
def delete_user(db_connection):
    def delete(id):
        try:
            cursor = db_connection.cursor()
            cursor.execute('DELETE FROM users WHERE id=%s', (id,))
            db_connection.commit()
            cursor.close()
            return 'User deleted', 200
        except Exception as e:
            db_connection.rollback()
            return str(e), 500
    return delete


# intake_users functions

def get_intake_users(db_connection):
    def get():
        try:
            cursor = db_connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM intake_users')
            rows = cursor.fetchall()
            cursor.close()
            return jsonify(rows), 200
        except Exception as e:
            return str(e), 500
    return get
    
def get_intake_user(db_connection):
    def get(id):
        try:
            cursor = db_connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM intake_users WHERE id=%s', (id,))
            row = cursor.fetchone()
            cursor.close()
            if not row:
                return 'Intake user not found', 404
            return jsonify(row), 200
        except Exception as e:
            return str(e), 500
    return get
    
def create_intake_user(db_connection):
    def post():
        try:
            data = request.json
            if not data or not all(key in data for key in ['user_id', 'HealthStatus', 'FatIntake', 'CaloryIntake', 'FiberIntake', 'CarbohidrateIntake', 'Feedback']):
                return 'Missing fields', 400
            cursor = db_connection.cursor()
            query = 'INSERT INTO intake_users (user_id, HealthStatus, FatIntake, CaloryIntake, FiberIntake, CarbohidrateIntake, Feedback) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            values = (data['user_id'], data['HealthStatus'], data['FatIntake'], data['CaloryIntake'], data['FiberIntake'], data['CarbohidrateIntake'], data['Feedback'])
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            return 'Intake user created', 201
        except Exception as e:
            db_connection.rollback()
            return str(e), 500
    return post
    
def update_intake_user(db_connection):
    def put(id):
        try:
            data = request.json
            if not data:
                return 'Missing fields', 400
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
            return 'Intake user updated', 200
        except Exception as e:
            db_connection.rollback()
            return str(e), 500
    return put
    
def delete_intake_user(db_connection):
    def delete(id):
        try:
            cursor = db_connection.cursor()
            cursor.execute('DELETE FROM intake_users WHERE id=%s', (id,))
            db_connection.commit()
            cursor.close()
            return 'Intake user deleted', 200
        except Exception as e:
            db_connection.rollback()
            return str(e), 500
    return delete
