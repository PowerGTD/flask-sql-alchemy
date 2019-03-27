import os
import sqlalchemy

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from models import db, Course, Member
from sqlalchemy import desc
  
app = Flask(__name__)
##Setting the place for the db to run
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sample-api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initializing the db (after registering the Models)
db.init_app(app)
#migration engine
migrate = Migrate(app, db)

@app.route('/courses')
def courses():
    courses = Course.query.all()
    response = []
    for c in courses:
        course = c.to_dict()
        response.append(course)
    
    return jsonify({"data": response})
    
@app.route('/courses/add', methods=['POST'])
def addcourse():
    info = request.get_json() or {}
    item = Course(name=info["name"])
    db.session.add(item)
    db.session.commit()
    return jsonify({"response": "ok"})
    
@app.route('/courses/<int:course_id>')
def hello(course_id):
    
    notfound = {
        'status_code': 400,
        'message': 'course not found'
    }
    
    if course_id != 0 and course_id is not None:
        currentCourse = Course.query.get(course_id)
        return jsonify(currentCourse.to_dict())
    else:
        return jsonify(notfound)
    
@app.route('/students')
def students():
    students = Member.query.all()
    response = []
    for s in students:
        student = s.to_dict()
        response.append(student)
        
    return jsonify({"data": response})
    
@app.route('/students/add', methods=['POST'])
def addstudent():
    info = request.get_json() or {}
    item = Member(first_name=info["first_name"],
                  last_name=info["last_name"],
                  course_id=info["course_id"],
                  age=info["age"])
    db.session.add(item)
    db.session.commit()
    return jsonify({"response": "ok"})
    
@app.route('/students/<int:student_id>', methods=['GET', 'PUT'])
def hello2(student_id):
    notfound = {
        'status_code': 400,
        'message': 'student not found'
    }
    if request.method == 'PUT':
        info = request.get_json() or {}
        if "course_id" in info:
            changeStudent = Member.query.get(student_id)
            changeStudent.course_id = info["course_id"]
            return jsonify(changeStudent.to_dict())
        else:
            return make_response(jsonify(notfound), 400)
    
    else:
        if student_id != 0 and student_id is not None:
            currentStudent = Member.query.get(student_id)
            return jsonify(currentStudent.to_dict())
        else:
            return jsonify(notfound)
 

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))