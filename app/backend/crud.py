from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os
import jwt
import json
import logging
import sys

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
CORS(app, support_credentials=True)
#app.config['CORS_HEADERS'] = 'Content-Type'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    #name = request.json['name']
    #password = request.json['password']
    
    #new_user = User(username, email)

    #db.session.add(new_user)
    #db.session.commit()

    #return jsonify(new_user)
    return "add_user"


# endpoint to update user
@app.route("/login", methods=["POST"])
@cross_origin(supports_credentials=True)
def login():
    
    encoded_jwt = jwt.encode({
        'name': request.form['name'],
        'password': request.form['name']
       }, 'secret', algorithm='HS256')    
    
    return encoded_jwt
    

# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    #return jsonify(result.data)
    return "blaaa"

# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)# -*- coding: utf-8 -*-

