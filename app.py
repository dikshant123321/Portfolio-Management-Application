from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# MySQL Configuration
# app.config['MYSQL_HOST'] = 'localhost'  
# app.config['MYSQL_USER'] = 'root'  
# app.config['MYSQL_PASSWORD'] = 'dikshant@1003' 
# app.config['MYSQL_DB'] = 'project'
app.config['MYSQL_HOST'] = 'containers-us-west-46.railway.app'  
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = 'rg2xnAS7e9BBQJA38BO0' 
app.config['MYSQL_DB'] = 'railway'  

mysql = MySQL(app)



# ========================================================PORTFOLIO_MANAGER====================================

@app.route('/create/portfolio_manager', methods=['POST'])
def create_user_profile():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    status=data.get('status')
    role=data.get('role')
    bio=data.get('bio')
    startdate=data.get('startdate')
    if name and email:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO portfolio_manager (name, email, status,role,bio,startdate) VALUES (%s, %s ,%s, %s,%s, %s)", (name, email, status,role,bio,startdate))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "User profile created successfully"}), 201
    return jsonify({"error": "fields are required"}), 400





@app.route('/get/portfolio_manager', methods=['GET'])
def get_user_profiles():
    cur = mysql.connection.cursor()
    cur.execute("SELECT pid, name, email, status, role, bio, startdate  FROM portfolio_manager")
    user_profiles = []
    columns = [col[0] for col in cur.description]  # Get column names from cursor description

    for row in cur.fetchall():
        user_profile_data = dict(zip(columns, row))
        user_profiles.append(user_profile_data)

    cur.close()
    return jsonify(user_profiles)




@app.route('/get/portfolio_manager/<int:managerId>', methods=['GET'])
def get_user_profiles_By_managerId(managerId):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM portfolio_manager WHERE pid = %s", (managerId,))
    user_profile_data = cur.fetchone() 

    if user_profile_data:
        columns = [col[0] for col in cur.description]  
        user_profile = dict(zip(columns, user_profile_data))
        cur.close()
        return jsonify(user_profile)

    cur.close()
    return jsonify({"message": "User profile not found"}), 404


@app.route('/update/portfolio_manager/<int:managerId>', methods=['PUT'])
def update_user_profile_by_manager_id(managerId):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    status=data.get('status')
    role=data.get('role')
    bio=data.get('bio')
    startdate=data.get('startdate')

    if name and email:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE portfolio_manager SET name = %s, email = %s, status = %s, role = %s, bio = %s, startdate = %s WHERE pid = %s", (name, email, status, role, bio, startdate, managerId))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "User profile updated successfully"}), 200
    else:
        return jsonify({"error": "Name and email fields are required"}), 400



@app.route('/delete/manager/<int:managerId>', methods=['DELETE'])
def delete_manager_by_manager_id(managerId):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM portfolio_manager WHERE pid = %s", (managerId,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "manager deleted successfully"}), 200



# ========================================================PROJECT====================================
@app.route('/create/project', methods=['POST'])
def create_project():
    data = request.get_json()
    projectname = data.get('projectname')
    status=data.get('status')
    startdate=data.get('startdate')
    enddate=data.get('enddate')
    managerid = data.get('managerid')
    if projectname and managerid and status and startdate and enddate:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  project (projectname, status, startdate, enddate,managerid) VALUES (%s, %s, %s, %s, %s)", (projectname, status, startdate, enddate,managerid))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Project created successfully"}), 201
    return jsonify({"error": "Project Name and manager_id fields are required"}), 400


@app.route('/get/project', methods=['GET'])
def get_projects():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM project")
    user_profiles = []
    columns = [col[0] for col in cur.description]  # Get column names from cursor description

    for row in cur.fetchall():
        user_profile_data = dict(zip(columns, row))
        user_profiles.append(user_profile_data)

    cur.close()
    return jsonify(user_profiles)



# 
@app.route('/api/getProjects/<int:managerId>', methods=['GET'])
def get_projects_by_managerid(managerId):
    cur = mysql.connection.cursor()
    cur.execute("SELECT projectid, projectname, status, startdate, enddate FROM project WHERE managerid = %s", (managerId,))
    projects = []
    rows = cur.fetchall()



    
    for row in rows:
        project_data = {
            "projectid": row[0],
            "projectname": row[1],
            "status": row[2],
            "startdate": row[3],
            "enddate": row[4]
        }
        projects.append(project_data)

    cur.close()
    return jsonify(projects)




@app.route('/get/project/<int:projectId>', methods=['GET'])
def get_project_By_projectId(projectId):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM project WHERE projectid = %s", (projectId,))
    project = cur.fetchall()
    cur.close()
    return jsonify(project)


@app.route('/update/project/<int:projectId>', methods=['PUT'])
def update_project_by_project_id(projectId):
    data = request.get_json()
    projectname = data.get('projectname')
    status = data.get('status')
    startdate = data.get('startdate')
    enddate = data.get('enddate')
    managerid = data.get('managerid')

    if projectname and status and startdate and enddate:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE project SET projectname = %s, status = %s, startdate = %s, enddate = %s ,managerid = %s WHERE projectid = %s", (projectname, status, startdate, enddate, managerid,projectId))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Project updated successfully"}), 200
    else:
        return jsonify({"error": "fields are required"}), 400



@app.route('/delete/project/<int:projectId>', methods=['DELETE'])
def delete_project_by_project_id(projectId):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM project WHERE projectid = %s", (projectId,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Project deleted successfully"}), 200


# ======================================================== TASK ====================================

@app.route('/create/task', methods=['POST'])
def create_task():
    data = request.get_json()
    taskname = data.get('taskname')
    description=data.get('description')
    assignto=data.get('assignto')
    status=data.get('status')
    projectid = data.get('projectid')
    if taskname and description and status and assignto and  projectid :
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  task (taskname, description, assignto, status ,projectid) VALUES (%s, %s, %s, %s, %s)", (taskname, description, assignto, status ,projectid))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Task created successfully"}), 201
    return jsonify({"error": "fields are required"}), 400


@app.route('/get/task', methods=['GET'])
def get_tasks():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM task")
    user_profiles = []
    columns = [col[0] for col in cur.description]  # Get column names from cursor description

    for row in cur.fetchall():
        user_profile_data = dict(zip(columns, row))
        user_profiles.append(user_profile_data)

    cur.close()
    return jsonify(user_profiles)


# SELECT * FROM task
@app.route('/get/task/<int:taskId>', methods=['GET'])
def get_task_By_taskId(taskId):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM task WHERE taskid = %s", (taskId,))
    task = cur.fetchall()
    cur.close()
    return jsonify(task)


@app.route('/update/task/<int:taskId>', methods=['PUT'])
def update_task_by_task_id(taskId):
    data = request.get_json()
    taskname = data.get('taskname')
    description=data.get('description')
    assignto=data.get('assignto')
    status=data.get('status')
    projectid = data.get('projectid')

    if taskname and status and description and assignto:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE task SET taskname = %s,  description = %s, assignto = %s, status= %s,  projectid= %s  WHERE taskid = %s", (taskname,  description, assignto, status,projectid,taskId))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Task updated successfully"}), 200
    else:
        return jsonify({"error": "fields are required"}), 400

@app.route('/delete/task/<int:taskId>', methods=['DELETE'])
def delete_task_by_task_id(taskId):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM task WHERE taskid = %s", (taskId,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Task deleted successfully"}), 200

# ======================================================== RESOURCE ====================================

@app.route('/create/resource', methods=['POST'])
def create_resource():
    data = request.get_json()
    name = data.get('name')
    description=data.get('description')
    type=data.get('type')
    availability=data.get('availability')
    assignedtaskid = data.get('assignedtaskid')
    if name and description and type and availability:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  resource (name, description, type, availability ,assignedtaskid) VALUES (%s, %s, %s, %s, %s)", (name, description, type, availability ,assignedtaskid))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "resource created successfully"}), 201
    return jsonify({"error": "fields are required"}), 400

@app.route('/get/resource', methods=['GET'])
def get_resource():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM resource")
    user_profiles = []
    columns = [col[0] for col in cur.description]  # Get column names from cursor description

    for row in cur.fetchall():
        user_profile_data = dict(zip(columns, row))
        user_profiles.append(user_profile_data)

    cur.close()
    return jsonify(user_profiles)
    


@app.route('/get/resource/<int:resourceId>', methods=['GET'])
def get_resource_By_resourceId(resourceId):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM resource WHERE resourceid = %s", (resourceId,))
    resource = cur.fetchall()
    cur.close()
    return jsonify(resource)

@app.route('/update/resource/<int:resourceId>', methods=['PUT'])
def update_resource_by_resource_id(resourceId):
    data = request.get_json()
    name = data.get('name')
    description=data.get('description')
    type=data.get('type')
    availability=data.get('availability')
    assignedtaskid = data.get('assignedtaskid')

    if name and type and description and availability:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE resource SET name = %s,  description = %s,  type = %s, availability= %s,  assignedtaskid = %s  WHERE resourceid = %s", (name,  description, type, availability, assignedtaskid, resourceId))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "resource updated successfully"}), 200
    else:
        return jsonify({"error": "fields are required"}), 400

@app.route('/delete/resource/<int:resourceId>', methods=['DELETE'])
def delete_resource_by_resource_id(resourceId):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM resource WHERE resourceid = %s", (resourceId,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Resource deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
