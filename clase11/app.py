import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "pat",
        "lastname": "card",
        "socialMedia":
        [
            {"facebookUser": "patcard"},
            {"instagramUser": "patcard"},
            {"xUser": "patcard"},
            {"linkedin": "patcard"},
            {"githubUser": "patcard"}
        ],
        "blog": "https://patcard.com",
        "author": "pat card"
    }
    return json.dumps(value)


