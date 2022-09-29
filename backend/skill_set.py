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
    