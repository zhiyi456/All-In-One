from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)

# Remember to add/remove the app config with your php password
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root:@localhost:3306/is212_all_in_one'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

import positions
import role
import course
import learning_journey
import registration
import skill_set
import skill
import skill_rewarded
import staff

db.create_all()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
