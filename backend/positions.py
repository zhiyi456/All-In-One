from flask import request, jsonify

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

    @app.route("/positions")
    def position_get_all():
        position_list = Positions.query.all()
        if position_list:
            return jsonify(
                {
                    "code": 200,
                    "data": {
                        "positions": [position.json() for position in position_list]
                    }
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There are no Positions."
            }
        ), 404

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

    @app.route("/get_position_by_ID/<Position_ID>")
    def get_position_by_ID(Position_ID):
        position_list = Positions.query.filter_by(Position_ID=Position_ID)
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
    
    @app.route("/create_new_position/<string:new_position>", methods=['POST'])
    def create_new_position(new_position):
        if (Positions.query.filter_by(Position_Name=new_position).first()):
            return jsonify(
                {
                    "code": 400,
                    "data": {
                        "Position_Name": new_position
                    },
                    "message": "Position already exists."
                }
            ), 400

        data = request.get_json()
        print(data)
        position = Positions(**data)
        print(position)
        try:
            db.session.add(position)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "Position_Name": position
                    },
                    "message": "An error occurred creating the Position."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": position.json()
            }
        ), 201


