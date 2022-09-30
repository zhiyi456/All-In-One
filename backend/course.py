from flask import jsonify

def create(app,db):
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

    @app.route("/course")
    def course_get_all():
        course_list = Course.query.all()
        if course_list:
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

    @app.route("/course_get_by_name/<name>")
    def course_get_by_name(name):
        course = Course.query.filter_by(course_name = name).first()
        if course:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "courses": course.json()
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There are no Courses."
            }
        ), 404