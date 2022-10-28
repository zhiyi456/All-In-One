import http
import unittest
from unittest.mock import patch, Mock
import flask
import requests
#from backend import app, course, learning_journey, positions, registration, role, skill_rewarded, skill_set, skill, staff
#from positions1 import *
#from backend1 import course1, positions1
#from backend.invokes import invoke_http, all_route
import positions
from positions import app
from collections import namedtuple


class TestBackend(unittest.TestCase):

    #set up only once at the start of running the test case
    # @classmethod
    # def setUpClass(cls):
    #     app = flask.Flask(__name__)
    #     with app.app_context():
    #         yield
    #     return app
    
    # #tear down after all test case ran
    # @classmethod
    # def tearDownClass(cls):
    #     pass
    
    # #run setup for every test case
    # def setUp(self):
    #     self.pst = positions1.Positions(20, 'Software Developer')
    #     #self.pst = Positions(20, 'Software Developer')

    # #run tear down for every end of test case
    # def tearDown(self):
    #     self.pst = None

    #test if existing position name can be added
    # def test_create_new_position(self):
    #     with app.test_request_context():
    #         with patch('flask.request.get_json') as mocked_get:
    #             mocked_get.return_value = {'Position_ID': 9, 'Position_Name':'test'}
    #             result = positions1.create_new_position('test')
    #             #result = create_new_position('Software Developer')
    #             self.assertEqual(result, 400)

    def test_position_get_all(self):
        with app.app_context():
            with patch('positions1.Positions') as mocked_get:
                # inst1 = positions1.Positions(1, "Data Analyst")
                # inst2 = positions1.Positions(2, "Human Resource")
                # inst3 = positions1.Positions(3, "Head of Security")
                #mock_return = [positions1.Positions(1, "Data Analyst"), positions1.Positions(2, "Human Resource"), positions1.Positions(3, "Head of Security")]
                mock_data = [
                    {   
                    "Position_ID": 1,
                    "Position_Name": "Data Analyst"
                    },
                    {
                    "Position_ID": 2,
                    "Position_Name": "Human Resource"
                    },
                    {
                    "Position_ID": 3,
                    "Position_Name": "Head of Security"
                    }]
                #print(mock_return)
                #converting dictionary to objects to simulate db
                mock_return = []
                for data in mock_data:
                    object_name = namedtuple("ObjectName", data.keys())(*data.values())
                    mock_return.append(object_name)
                expected_result = flask.jsonify({
                    "code": 200,
                    "data": {
                        "positions": [
                        {
                            "Position_ID": 1,
                            "Position_Name": "Data Analyst"
                        },
                        {
                            "Position_ID": 2,
                            "Position_Name": "Human Resource"
                        },
                        {
                            "Position_ID": 3,
                            "Position_Name": "Head of Security"
                        }
                        ]
                    }
                    })
                mocked_get.query.all.return_value = mock_return
                result = positions1.position_get_all()
                # print(fake_return)
                #print(result)
                self.maxDiff = None
                self.assertEqual(result.data, expected_result.data)

    def test_position_by_name(self):
        with app.app_context():
            with patch('positions1.Positions') as mocked_get:
                # inst1 = positions1.Positions(1, "Data Analyst")
                # inst2 = positions1.Positions(2, "Human Resource")
                # inst3 = positions1.Positions(3, "Head of Security")
                #mock_return = [positions1.Positions(1, "Data Analyst"), positions1.Positions(2, "Human Resource"), positions1.Positions(3, "Head of Security")]
                mock_data = [
                    {   
                    "Position_ID": 1,
                    "Position_Name": "Data Analyst"
                    }]
                #print(mock_return)
                #converting dictionary to objects to simulate db
                mock_return = []
                for data in mock_data:
                    object_name = namedtuple("ObjectName", data.keys())(*data.values())
                    mock_return.append(object_name)
                expected_result = flask.jsonify({
                    "code": 200,
                    "data": {
                        "Positions": [
                        {
                            "Position_ID": 1,
                            "Position_Name": "Data Analyst"
                        }
                        ]
                    }
                    })
                mocked_get.query.filter_by.return_value = mock_return
                result = positions1.get_position_by_name("Data Analyst")
                # print(fake_return)
                print(result)
                self.maxDiff = None
                self.assertEqual(result.data, expected_result.data)

    def test_position_by_ID(self):
        with app.app_context():
            with patch('positions1.Positions') as mocked_get:
                # inst1 = positions1.Positions(1, "Data Analyst")
                # inst2 = positions1.Positions(2, "Human Resource")
                # inst3 = positions1.Positions(3, "Head of Security")
                #mock_return = [positions1.Positions(1, "Data Analyst"), positions1.Positions(2, "Human Resource"), positions1.Positions(3, "Head of Security")]
                mock_data = [
                    {   
                    "Position_ID": 1,
                    "Position_Name": "Data Analyst"
                    }]
                #print(mock_return)
                #converting dictionary to objects to simulate db
                mock_return = []
                for data in mock_data:
                    object_name = namedtuple("ObjectName", data.keys())(*data.values())
                    mock_return.append(object_name)
                expected_result = flask.jsonify({
                    "code": 200,
                    "data": {
                        "Positions": [
                        {
                            "Position_ID": 1,
                            "Position_Name": "Data Analyst"
                        }
                        ]
                    }
                    })
                mocked_get.query.filter_by.return_value = mock_return
                result = positions1.get_position_by_ID(1)
                # print(fake_return)
                print(result)
                self.maxDiff = None
                self.assertEqual(result.data, expected_result.data)



#allow us to run the whole test suite by running - python test_unittest.py
#UPDATE: don't have to cd test just run: python -m unittest test.test_unittest
if __name__ == '__main__':
    unittest.main()