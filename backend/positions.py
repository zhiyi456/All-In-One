from flask import jsonify


def create(app, db):
    class Positions(db.Model):
        __tablename__ = 'Positions'

        Position_ID = db.Column(db.Integer, primary_key=True)
        Position_Name = db.Column(db.String(50))

        def __init__(self, Position_ID, Position_Name):
            self.Position_ID = Position_ID
            self.Position_Name = Position_Name

        def json(self):
            return {"Position_ID": self.Position_ID, "Position_Name": self.Position_Name}

    @app.route("/get_position_by_name/<Position_Name>")
    def get_position_by_name(Position_Name):
        position_list = Positions.query.filter_by(Position_Name=Position_Name)
        if position_list:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "Positions": [position.json() for position in position_list]
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "Position is not found. Please double check."
            }
        ), 404
