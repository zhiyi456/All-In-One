from flask import jsonify


def create(app, db):
    class Skill(db.Model):
        __tablename__ = 'Skill'

        Skill_Name = db.Column(db.String(50), primary_key=True)

        def __init__(self, Skill_Name):
            self.Skill_Name = Skill_Name

        def json(self):
            return {"Skill_Name": self.Skill_Name}
