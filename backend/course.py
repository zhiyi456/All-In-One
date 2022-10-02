from flask import jsonify
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ



def create(app, db):
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

    @app.route("/course/name/<string:course_name>", methods=['GET'])
    def course_get_by_name(course_name):
        course_data = Course.query.filter_by(course_name = course_name).first()
        if course_data:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "courses": course_data.json()
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": 'No course named ' +str(course_name) 
            }
        ), 404

    @app.route("/course/id/<string:course_id>", methods=['GET'])
    def course_get_by_course_id(course_id):
        course = Course.query.filter_by(course_id = course_id).first()
        if course:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "course": course.json()
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": str(course_id) + "id not found."
            }
        ), 404
