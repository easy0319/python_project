from flask import Blueprint, request, render_template, session, redirect, url_for
from .db import connect_mongo, usersDAO

db_connection = connect_mongo.ConnectDB().db
users = usersDAO.Users(db_connection)

usersAPI = Blueprint('usersAPI', __name__, template_folder='templates')

@usersAPI.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		if 'userEmail' in session:
			info = session['userEmail'].split('@')
			return render_template('welcome.html', info = info[0])
		else:
			return render_template('signup.html')
	
	if request.method == 'POST':
		if 'userEmail' in session:	
			info = session['userEmail'].split('@')
			return render_template('welcome.html', info = info[0])
		else:
			if users.userCreate(request.form.to_dict(flat='true')):
				session['userEmail'] = request.form['userEmail']
				info = session['userEmail'].split('@')
				return render_template('welcome.html', info = info[0])
			else:
				return render_template('signup.html')

@usersAPI.route('/')
@usersAPI.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'GET':
		if 'userEmail' in session:
			info = session['userEmail'].split('@')
			return render_template('welcome.html', info = info[0])
		else:
			return render_template('signin.html')

	if request.method == 'POST':
		if 'userEmail' in session:
			info = session['userEmail'].split('@')
			return render_template('welcome.html', info = info[0])
		else:
			if users.userAuthentication(request.form.to_dict(flat='true')):
				session['userEmail'] = request.form['userEmail']
				info = session['userEmail'].split('@')
				return render_template('welcome.html', info = info[0])
			else:
				return render_template('signin.html')
				

@usersAPI.route('/logout')
def logout():
	if 'userEmail' in session:
		session.pop('userEmail')
		return render_template('welcome.html')
	return redirect(url_for('usersAPI.signin'))
