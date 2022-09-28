from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)

# Remember to add/remove the app config with your php password
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:@localhost:3306/is212_all_in_one'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Role(db.Model):
    tablename = 'Role'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20), nullable=False)

    def __init__(self, role_id, role_name):
        self.role_id = role_id
        self.role_name = role_name

    def json(self):
        dto = {
            'role_id': self.role_id,
            'role_name': self.role_name,
        }

        return dto

class Staff(db.Model):
    tablename = 'Staff'

    staff_id = db.Column(db.Integer, primary_key=True)
    staff_fname = db.Column(db.String(32), nullable=False)
    staff_lname = db.Column(db.String(32), nullable=False)
    dept = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    role = db.Column(db.String(32), nullable=False)

    def __init__(self, staff_id, staff_fname, staff_lname, dept, email, role):
        self.staff_id = staff_id
        self.staff_fname = staff_fname
        self.staff_lname = staff_lname
        self.dept = dept
        self.email = email
        self.role = role

    def json(self):
        dto = {
            'staff_id': self.staff_id,
            'staff_fname': self.staff_fname,
            'staff_lname': self.staff_lname,
            'dept': self.dept,
            'email': self.email,
            'role': self.role,
        }
        return dto

class Course(db.Model):
    tablename = 'Course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(32), nullable=False)
    course_desc = db.Column(db.String(32), nullable=False)
    course_status = db.Column(db.String(32), nullable=False)
    course_type = db.Column(db.String(32), nullable=False)
    course_category = db.Column(db.String(32), nullable=False)

    def __init__(self, course_id, course_name, course_desc, course_status, course_type, course_category):
        self.course_id = course_id
        self.course_name = course_name
        self.course_desc = course_desc
        self.course_status = course_status
        self.course_type = course_type
        self.course_category = course_category

    def json(self):
        dto = {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'course_desc': self.course_desc,
            'course_status': self.course_status,
            'course_type': self.course_type,
            'course_category': self.course_category,
        }

        return dto

class Registration(db.Model):
    tablename = 'Course'

    reg_id = db.Column(db.Integer, primary_key=True)
    reg_status = db.Column(db.String(32), nullable=False)
    completion_status = db.Column(db.String(32), nullable=False)
    course_id = db.Column(db.String(32), nullable=False)
    staff_id = db.Column(db.String(32), nullable=False)

    def __init__(self, reg_id, reg_status, completion_status, course_id, staff_id):
        self.reg_id = reg_id
        self.reg_status = reg_status
        self.completion_status = completion_status
        self.course_id = course_id
        self.staff_id = staff_id
    
    def json(self):
        dto = {
            'reg_id': self.reg_id,
            'reg_status': self.reg_status,
            'completion_status': self.completion_status,
            'course_id': self.course_id,
            'staff_id': self.staff_id,
        }

        return dto

class Positions(db.Model):
    __tablename__ = 'Positions'

    Position_ID = db.Column(db.Integer, primary_key=True)
    Position_Name = db.Column(db.String(50))

    def __init__(self, Position_ID, Position_Name):
        self.Position_ID = Position_ID
        self.Position_Name = Position_Name
 
    def json(self):
        return {"Position_ID": self.Position_ID, "Position_Name": self.Position_Name}


class Skill(db.Model):
    __tablename__ = 'Skill'

    Skill_Name = db.Column(db.String(50), primary_key=True)

    def __init__(self, Skill_Name):
        self.Skill_Name = Skill_Name

 
    def json(self):
        return {"Skill_Name": self.Skill_Name}

class Skill_Set(db.Model):
    __tablename__ = 'Skill_Set'

    Skill_Set_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(50), db.ForeignKey('Skill.Skill_Name'))
    Position_ID = db.Column(db.Integer, db.ForeignKey('Positions.Position_ID'))

    def __init__(self, Skill_Set_ID, Skill_Name, Position_ID):
        self.Skill_Set_ID = Skill_Set_ID
        self.Skill_Name = Skill_Name
        self.Position_ID = Position_ID

    def json(self):
        return {"Skill_Set_ID": self.Skill_Set_ID, "Skill_Name": self.Skill_Name, "Position_ID": self.Position_ID}


class Skill_Rewarded(db.Model):
    __tablename__ = 'Skill_Rewarded'

    Skill_Rewarded_ID = db.Column(db.Integer, primary_key=True)
    Skill_Name = db.Column(db.String(50), db.ForeignKey('Skill.Skill_Name'))
    Course_ID = db.Column(db.String(20), db.ForeignKey('Course.Cosition_ID'))

    def __init__(self, Skill_Rewarded_ID, Skill_Name, Course_ID):
        self.Skill_Rewarded_ID = Skill_Rewarded_ID
        self.Skill_Name = Skill_Name
        self.Course_ID = Course_ID

    def json(self):
        return {"Skill_Rewarded_ID": self.Skill_Rewarded_ID, "Skill_Name": self.Skill_Name, "Course_ID": self.Course_ID}


@app.route("/skill_set")
def get_all():
    skill_set = Skill_Set.query.all()
    if len(skill_set):
        return jsonify(
            {  
                "code": 200,
                "data": {
                    "skill_set": [skill.json() for skill in skill_set]
                }
            }
        )
    else:
        return jsonify({
            "message": "Skill set not found."
        }), 404


db.create_all()


@app.route("/role")
def role_get_all():
    role_list = Role.query.all()
    print(len(role_list))
    if len(role_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "roles": [role.json() for role in role_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Roles."
        }
    ), 404

@app.route("/staff")
def staff_get_all():
    staff_list = Staff.query.all()
    if len(staff_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staffs": [staff.json() for staff in staff_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Staffs."
        }
    ), 404

@app.route("/course")
def course_get_all():
    course_list = Course.query.all()
    if len(course_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "courses": [course.json() for course in course_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Courses."
        }
    ), 404


@app.route("/registration")
def registration_get_all():
    registration_list = Registration.query.all()
    if len(registration_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "registrations": [registration.json() for registration in registration_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no registrations."
        }
    ), 404

# Read Course Skills
@app.route("/view_course_skills/<Course_ID>")
def view_course_skills(Course_ID):
    skill_rewarded_list = Skill_Rewarded.query.filter_by(Course_ID = Course_ID)
    if len(skill_rewarded_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "Skill_Rewarded": [skill_rewarded.json() for skill_rewarded in skill_rewarded_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course ID is not found. Please double check."
        }
    ), 404



# @app.route("/delete_booking/<BookingID>")
# def delete_patient_booking(BookingID):
#     booking = Booking.query.filter_by(BookingID = BookingID).first()
#     if booking:
#         db.session.delete(booking)
#         db.session.commit()
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": {
#                     "BookingID": BookingID
#                 }
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "data": {
#                 "BookingID": BookingID
#             },
#             "message": "Booking not found."
#         }
#     ), 404

# @app.route("/check_booking")
# def check_booking():
#     BookingID = request.json.get("BookingID", None)
#     booking = Booking.query.filter_by(BookingID = BookingID).first()
#     if booking:
#         return jsonify(
#             {
#                 "code": 200,
#                 "data": booking.json()
#             }
#         )
#     return jsonify(
#         {
#             "code": 404,
#             "message":"Such booking does not exist."
#         }
#     )

# @app.route("/booking/<string:BookingID>", methods=['POST'])
# def create_booking(BookingID):
#     if (Booking.query.filter_by(BookingID=BookingID).first()):
#         return jsonify(
#             {
#                 "code": 400,
#                 "data": {
#                     "BookingID": BookingID
#                 },
#                 "message": "Booking already exists."
#             }
#         ), 400

#     data = request.get_json()
#     booking = Booking(BookingID, **data)

#     try:
#         db.session.add(booking)
#         db.session.commit()
#     except:
#         return jsonify(
#             {
#                 "code": 500,
#                 "data": {
#                     "BookingID": BookingID
#                 },
#                 "message": "An error occurred creating the booking."
#             }
#         ), 500

#     return jsonify(
#         {
#             "code": 201,
#             "data": booking.json()
#         }
#     ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)