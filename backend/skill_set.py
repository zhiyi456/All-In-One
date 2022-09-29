from flask import jsonify

def create(app,db):
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
        
        @app.route("/skill_set") #get all skill sets
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
        
        @app.route("/skill_set/<Position_ID>") #get skills by position_ID
        def get_skills_by_position(Position_ID):
            skill_set_list = Skill_Set.query.filter_by(Position_ID = Position_ID)
            if skill_set_list:
                return jsonify(
                    {
                        "code": 200,
                        "data": {
                            "Skill_Set": [skill_set.json() for skill_set in skill_set_list]
                        }
                    }
                )
            return jsonify(
                {
                    "code": 404,
                    "message": "Position ID is not found. Please double check."
                }
            ), 404
    