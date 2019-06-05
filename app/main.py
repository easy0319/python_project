#flask
from flask import Flask
from view.usersAPI import usersAPI
from view.postsAPI import postsAPI
import json

app = Flask(__name__)

with open('mykey.json') as Json:
	app.secret_key = json.loads(Json.read())['key']


#route
app.register_blueprint(usersAPI)
app.register_blueprint(postsAPI)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000);
