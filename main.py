from flask import Flask, request, redirect, url_for, jsonify  # flash render_template
import pymongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import requests
import re
import json


client = pymongo.MongoClient('mongodb+srv://dbUser:o5jzqcHzuKacB2Y1@lunchbox.1pvyu.mongodb.net/lunchbox?retryWrites=true&w=majority')
database = client.mylunch


app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xd9\xb9\x07\xad\x9d[\xe0e\xd2\x84\x9eU\xd8s\xe0\x15W\xcf\xf2n\x93\x01\xdc\xe4'  # 要換
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=180)


@app.route('/')
def index():
    return 'hi~ This is myschool-mylunch(temporary name)'


@app.route('/verify-token', methods=['GET','POST'])
def verify_token():
    token = request.args.get('token')
    data = json.dumps({'token' : str(token)})
    res = requests.post('https://myschool-account.herokuapp.com/token/verify', data = data)
    return res.text


if __name__ == "__main__":
    app.run()
