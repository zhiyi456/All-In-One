import unittest
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
import flask_testing
import json


app = Flask(__name__)
db = SQLAlchemy(app)



class TestApp(flask_testing.TestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.session.add(Positions('Human Resource'))
        db.session.add(Positions('Analyst'))
        db.session.add(Positions('Head of Security'))
        #db.session.commit()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

from positions import Positions

class TestPositions(TestApp):    
    def test_create_new_position(self):
        
        new_position = Positions(Position_Name= 'Software Developer')
        db.session.add(new_position)
        db.session.commit()

        request_body = {
            'Position_Name': new_position.Position_Name
        }

        response = self.client.post("/create_new_position/"+new_position.Position_Name,
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        #print(response.data)
        self.assertEqual(response.data, jsonify(
        {
            "code": 201,
            "data": {
            'Position_Name': new_position.Position_Name
        }
        }
        ).data)
    
    def test_create_existing_position(self):
        new_position = Positions(Position_Name= 'Head of Security')
        # db.session.add(new_position)
        # db.session.commit()

        request_body = {
            'Position_Name': new_position.Position_Name
        }

        response = self.client.post("/create_new_position/"+new_position.Position_Name,
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        #print(response.data)
        self.maxDiff = None
        self.assertEqual(response.data, jsonify(
        {
            "code": 400,
            "data": {"Position_Name":"Head of Security"},
            "message":"Position already exists."}
        ).data)

    def test_get_all_position(self):
        response = self.client.get("/positions")
        #print(response.data)
        self.assertEqual(response.data, jsonify(
            {
            "code": 200,
            "data": {
                "positions": [
                {
                    "Position_Name": "Human Resource"
                },
                {
                    "Position_Name": "Analyst"
                },
                {
                    "Position_Name": "Head of Security"
                }
                ]
            }
            }
        ).data)

    #optional
    def test_get_all_position_length(self):
        response = self.client.get("/positions")
        #print(response.data)
        response = response.data.decode('utf-8')
        response = json.loads(response)
        self.assertEqual(len(response['data']['positions']), 3)

    def test_get_position_by_name(self):
        response = self.client.get("/get_position_by_name/Head of Security")
        #print(response.data)
        self.assertEqual(response.data, jsonify(
            {
            "code": 200,
            "data": {
                "Positions": [
                {
                    "Position_Name": "Head of Security"
                }
                ]
            }
            }
        ).data)




#allow us to run the whole test suite by running - python test_unittest.py
#UPDATE: don't have to cd test just run: python -m unittest test.test_unittest
if __name__ == '__main__':
    unittest.main()