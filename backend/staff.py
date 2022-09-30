from flask import jsonify


def create(app, db):
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
