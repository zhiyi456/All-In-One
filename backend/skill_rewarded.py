from flask import jsonify
from invokes import invoke_http

def create(app, db):
    class Skill_Rewarded(db.Model):
        __tablename__ = 'Skill_Rewarded'

        Skill_Rewarded_ID = db.Column(db.Integer, primary_key=True)
        Skill_ID = db.Column(
            db.String(50), db.ForeignKey('Skill.Skill_ID'))
        Course_ID = db.Column(
            db.String(20), db.ForeignKey('Course.Cosition_ID'))

        def __init__(self, Skill_Rewarded_ID, Skill_ID, Course_ID):
            self.Skill_Rewarded_ID = Skill_Rewarded_ID
            self.Skill_ID = Skill_ID
            self.Course_ID = Course_ID

        def json(self):
            return {"Skill_Rewarded_ID": self.Skill_Rewarded_ID, "Skill_ID": self.Skill_ID, "Course_ID": self.Course_ID}

    @app.route("/view_course_skills/get_skill/<Course_ID>")
    def view_course_skills(Course_ID):
        skill_rewarded_list = Skill_Rewarded.query.filter_by(Course_ID=Course_ID)
        if skill_rewarded_list:
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

    @app.route("/view_course_skills/get_course/<Skill_Name>")
    def view_course_by_skillID(Skill_Name):
        #get skill data
        course_route = "http://127.0.0.1:5000/skill"
        skills = invoke_http(course_route, method='GET')
        for skill in skills['data']['skill']:
            print(skill)
            if (skill['Skill_Name'] == Skill_Name):
                Skill_ID = skill['Skill_ID']

        course_id_list = Skill_Rewarded.query.filter_by(Skill_ID=Skill_ID)
        if course_id_list:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "Skill_Rewarded": [skill_rewarded.json() for skill_rewarded in skill_rewarded_list]
                    }
                }
            )
        # course_id_list = Skill_Rewarded.query.filter_by(Skill_ID=id)
        # if course_id_list:
        #    # print('-------------I AM PRINTING SOMETHING!--------------')
        #     print(list(skill_rewarded.json() for skill_rewarded in course_id_list))
        #    # print('--------------I AM NO LONGER PRINTIGN!=---------------')
        #     result = invoke_http("http://127.0.0.1:5000"+"/course/multiple_course_id?course_id_list={course_id_list}", method='GET', json=None)
        #     print('order_result:', result)
        #     return jsonify(result)
        return jsonify(
            {
                "code": 404,
                "message": "No course is associated with " + str(Skill_ID)
            }
        ), 404




    # @app.route("/view_course_skills/get_course/<Skill_Name>")
    # def view_course_by_skills(Skill_Name):
    #     course_id_list = Skill_Rewarded.query.filter_by(Skill_Name=Skill_Name)
    #     if course_id_list:
    #         return jsonify(
    #             {
    #                 "code": 200,
    #                 "data": {
    #                     "Course List": [course.json() for course in course_id_list]
    #                 }
    #             }
    #         )
    #     return jsonify(
    #         {
    #             "code": 404,
    #             "message": "No course is associated with " + str(Skill_Name)
    #         }
    #     ), 404