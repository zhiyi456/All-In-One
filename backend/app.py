from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
import role, course, learning_journey, positions, registration, skill_set, skill, skills_rewarded, staff

app = Flask(__name__)

# Remember to add/remove the app config with your php password
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root:@localhost:3306/is212_all_in_one'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

if __name__ == '__main__':
    role.create(app,db)
    staff.create(app,db)
    course.create(app,db)
    positions.create(app,db)
    registration.create(app,db)
    skill.create(app,db)
    skill_set.create(app,db)
    skills_rewarded.create(app,db)
    # learning_journey.create(app,db)
    db.create_all()
    
    app.run(host='0.0.0.0', port=5000, debug=True)
