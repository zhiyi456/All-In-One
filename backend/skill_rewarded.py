from flask import jsonify
from __main__ import app,db


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




@app.route("/view_course_skills/get_course/<Skill_ID>")
def view_course_by_skill_id(Skill_ID):
    skill_rewarded_list = Skill_Rewarded.query.filter_by(Skill_ID=Skill_ID)
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
                "message": "No course is associated"
            }
        ), 404
     