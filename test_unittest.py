import unittest
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
# from backend import app, course, learning_journey, positions, registration, role, skill_rewarded, skill_set, skill, staff
from backend import course

class TestBackend(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_course_get_all(self):
        result = course
        print(result)
        data = []
        self.assertEqual(result, data)


#allow us to run the whole test suite by running - python test_unittest.py
if __name__ == '__main__':
    TestBackend.test_course_get_all()
    unittest.main()