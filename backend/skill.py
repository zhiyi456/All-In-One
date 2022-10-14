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

    @app.route("/skill/name/<string:name>", methods=['GET'])
    def skill_get_by_name(name):
        skill_data = Skill.query.filter_by(Skill_Name = name).first()
        if skill_data:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "skills": skill_data
                    }
                }
            )
        return jsonify (
            {
                "code": 404,
                "message": 'No skill named ' + str(name) 
            }
        )

    @app.route("/skill/<Skill_ID>", methods=['GET'])
    def get_skill_by_id(Skill_ID):
        skill_data = Skill.query.filter_by(Skill_ID=Skill_ID)
        if skill_data:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "skill": [skill.json() for skill in skill_data]
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "Skill ID is not found. Please double check."
            }
        ), 404
