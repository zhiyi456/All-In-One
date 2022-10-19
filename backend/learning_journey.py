from flask import request, jsonify
from __main__ import app,db

class LearningJourney(db.Model):
    __tablename__ = 'Learning_Journey'
        
    Learning_Journey_ID = db.Column(db.Integer, primary_key=True)
    Staff_ID = db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'))
    Skill_Set_ID = db.Column(db.Integer, db.ForeignKey('Skill_Set.Skill_Set_ID'))
    Skill_Rewarded_ID = db.Column(db.Integer, db.ForeignKey('Skill_Rewarded.Skill_Rewarded_ID'))

    def __init__(self,Staff_ID, Skill_Set_ID, Skill_Rewarded_ID):
        self.Staff_ID = Staff_ID
        self.Skill_Set_ID = Skill_Set_ID
        self.Skill_Rewarded_ID = Skill_Rewarded_ID


    def json(self):
        return {
            "Learning_Journey_ID": self.Learning_Journey_ID,
            "Staff_ID": self.Staff_ID,
            "Skill_Set_ID": self.Skill_Set_ID,
            "Skill_Rewarded_ID": self.Skill_Rewarded_ID,
        }

@app.route("/get_learning_journey")
def get_learning_journey():
    lj_list = LearningJourney.query.all()
    if len(lj_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lj": [lj.json() for lj in lj_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Learning Journey."
        }
    ), 404


@app.route("/get_learning_journey_by_staff_id/<Staff_ID>")
def get_learning_journey_by_staff_id(Staff_ID):
    lj_list = LearningJourney.query.filter_by(Staff_ID=Staff_ID).all()
    if len(lj_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lj": [lj.json() for lj in lj_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Learning Journey."
        }
    ), 404


@app.route("/get_learning_journey_by_lj_id/<Learning_Journey_ID>")
def get_learning_journey_by_lj_id(Learning_Journey_ID):
    lj_list = LearningJourney.query.filter_by(Learning_Journey_ID=Learning_Journey_ID).all()

    if len(lj_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lj": [lj.json() for lj in lj_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no Learning Journey."
        }
    ), 404

@app.route("/create_learning_journey", methods=['POST'])
def create_learning_journey():

    data = request.get_json()
    lj = LearningJourney(**data)
    db.session.add(lj)
    db.session.commit()
    try:
        print("Hello")
        
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "Learning_Journey": data
                },
                "message": "An error occurred creating the Learning Journey."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": data
        }
    ), 201


    