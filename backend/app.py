from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)

# Remember to add/remove the app config with your php password
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/booking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

@app.route("/booking")
def get_all():
    booking_list = Booking.query.all()
    if len(booking_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookings": [booking.json() for booking in booking_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no bookings."
        }
    ), 404

@app.route("/booking/<string:NRIC>")
def get_patient_booking(NRIC):
    patient_booking_list = Booking.query.filter_by(NRIC = NRIC).all()
    if len(patient_booking_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "bookings": [booking.json() for booking in patient_booking_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no bookings by this NRIC."
        }
    ), 404

@app.route("/delete_booking/<BookingID>")
def delete_patient_booking(BookingID):
    booking = Booking.query.filter_by(BookingID = BookingID).first()
    if booking:
        db.session.delete(booking)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "BookingID": BookingID
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "BookingID": BookingID
            },
            "message": "Booking not found."
        }
    ), 404

@app.route("/check_booking")
def check_booking():
    BookingID = request.json.get("BookingID", None)
    booking = Booking.query.filter_by(BookingID = BookingID).first()
    if booking:
        return jsonify(
            {
                "code": 200,
                "data": booking.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message":"Such booking does not exist."
        }
    )

@app.route("/booking/<string:BookingID>", methods=['POST'])
def create_booking(BookingID):
    if (Booking.query.filter_by(BookingID=BookingID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "BookingID": BookingID
                },
                "message": "Booking already exists."
            }
        ), 400

    data = request.get_json()
    booking = Booking(BookingID, **data)

    try:
        db.session.add(booking)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "BookingID": BookingID
                },
                "message": "An error occurred creating the booking."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": booking.json()
        }
    ), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)