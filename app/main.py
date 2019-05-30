from flask import Flask
from view.usersAPI import usersAPI
import json

app = Flask(__name__)

with open('mykey.json') as Json:
    app.secret_key = json.loads(Json.read())['key']

app.register_blueprint(usersAPI)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000);
