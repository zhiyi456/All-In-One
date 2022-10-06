#from urllib import request
import json
from flask import jsonify
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ



def create(app, db):
    class LearningJourney(db.Model):
        __tablename__ = 'Learning_Journey'
         
        Learning_Journey_ID = db.Column(db.Integer, primary_key=True)
        Staff_ID = db.Column(
            db.Integer, db.ForeignKey('Staff.Staff_ID'))
        Skill_Set_ID = db.Column(
            db.Integer, db.ForeignKey('Skill_Set.Skill_Set_ID'))
        Skill_Rewarded_ID = db.Column(
            db.Integer, db.ForeignKey('Skill_Rewarded.Skill_Rewarded_ID'))

        def __init__(self,staff_id, skill_set_id, skill_rewarded_id):
            self.Staff_ID = staff_id
            self.Skill_Set_ID = skill_set_id
            self.Skill_Rewarded_ID = skill_rewarded_id
  

        def json(self):
            dto = {
                'Learning_Journey_ID': self.Learning_Journey_ID,
                'Staff_ID': self.Staff_ID,
                'Skill_Set_ID': self.Skill_Set_ID,
                'Skill_Rewarded_ID': self.Skill_Rewarded_ID,
            }
            return dto

    @app.route("/create_learning_journey",methods=['POST'])
    def create_learning_journey():
        data = request.get_json()
        print('PLEASEZ!!!!!!')
        print(data)
        print('-----------------------------------------------')
        print('-----------------------------------------------')
        print('-----------------------------------------------')

        lj = LearningJourney(**data)
        
        print(lj)
        try:
            db.session.add(lj)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "Learning_Journey": lj
                    },
                    "message": "An error occurred creating the Learning Journey."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": lj.json()
            }
        ), 201


        