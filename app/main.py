#flask
from flask import Flask
from view.postsAPI import postsAPI
from view.usersAPI import usersAPI
from view.profileAPI import profileAPI
import json

app = Flask(__name__)

with open('mykey.json') as Json:
	app.secret_key = json.loads(Json.read())['key']


#route
app.register_blueprint(postsAPI)
app.register_blueprint(usersAPI)
app.register_blueprint(profileAPI)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000);
