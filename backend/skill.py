from flask import jsonify


def create(app, db):
    class Skill(db.Model):
        __tablename__ = 'Skill'

        Skill_ID = db.Column(db.Integer, primary_key=True)
        Skill_Name = db.Column(db.String(50))

        def __init__(self, Skill_ID, Skill_Name):
            self.Skill_ID = Skill_ID
            self.Skill_Name = Skill_Name

        def json(self):
            return {"Skill_Name": self.Skill_Name, "Skill_ID": self.Skill_ID}




        @app.route("/skills")
        def skill_get_all():
            skill_list = Skill.query.all()
            if skill_list:
                return jsonify(
                    {
                        "code": 200,
                        "data": {
                            "skills": [skill.json() for skill in skill_list]
                        }
                    }
                )
            return jsonify(
                {
                    "code": 404,
                    "message": "There are no Skills."
                }
            ), 404



        # @app.route("/course/id/<string:course_id>", methods=['GET'])
        # def course_get_by_course_id(course_id):
        #     course = Course.query.filter_by(course_id = course_id).first()
        #     if course:
        #         return jsonify(
        #             {
        #                 "code": 200,
        #                 "data": {
        #                     "course": course.json()
        #                 }
        #             }
        #         )
        #     return jsonify(
        #         {
        #             "code": 404,
        #             "message": str(course_id) + "id not found."
        #         }
        #     ), 404


        @app.route("/skill/name/<string:name>", methods=['GET'])
        def skill_get_by_name(name):
            skill_data = Skill.query.filter_by(Skill_Name = name).first()
            if skill_data:
                return jsonify(
                    {
                        "code": 200,
                        "data": {
                            "skills": skill_data.json()
                        }
                    }
                )
            return jsonify(
                {
                    "code": 404,
                    "message": 'No skill named ' +str(name) 
                }
            ), 404