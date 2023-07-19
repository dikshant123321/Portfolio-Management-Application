from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = 'dikshant@1003' 
app.config['MYSQL_DB'] = 'project'  

mysql = MySQL(app)

@app.route('/')
def index():
    return "Welcome to Project Prism!"



@app.route('/create/user_profiles', methods=['POST'])
def create_user_profile():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name and email:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_profiles (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "User profile created successfully"}), 201
    return jsonify({"error": "Name and email fields are required"}), 400


@app.route('/get/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    name = data.get('name')
    manager_id = data.get('manager_id')
    if name and manager_id:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  projects (name, manager_id) VALUES (%s, %s)", (name, manager_id))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Project created successfully"}), 201
    return jsonify({"error": "Project Name and manager_id fields are required"}), 400


@app.route('/get/user_profiles', methods=['GET'])
def get_user_profiles():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user_profiles")
    user_profiles = cur.fetchall()
    cur.close()
    return jsonify(user_profiles)


@app.route('/get/projects', methods=['GET'])
def get_projects():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM projects")
    projects = cur.fetchall()
    cur.close()
    return jsonify(projects)

if __name__ == '__main__':
    app.run(debug=True)
