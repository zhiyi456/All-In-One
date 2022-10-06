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

    @app.route("/skill")  # get all skill
    def skill_get_all():
        skills = Skill.query.all()
        if len(skills):
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "skill": [skill.json() for skill in skills]
                    }
                }
            )
        else:
            return jsonify({
                "message": "Skills not found."
            }), 404