from flask import Blueprint, request, render_template, session, redirect, url_for
from .db import connect_mongo, postsDAO

db_connection = connect_mongo.ConnectDB().db
posts = postsDAO.Posts(db_connection)

postsAPI = Blueprint('postsAPI', __name__, template_folder='templates')

@postsAPI.route('/post')
def post():
    if 'userEmail' in session:
        info = session['userEmail'].split('@')
        return render_template('post.html', info = info[0])
    else:
        post = posts.postValidation()
        return render_template('welcome.html', post = post)

@postsAPI.route('/', methods=['GET'])
def base():
    if request.method == 'GET':
        if 'userEmail' in session:
            post = posts.postValidation()
            info = session['userEmail'].split('@')
            return render_template('welcome.html', info = info[0], post = post)
        else:
            post = posts.postValidation()
            return render_template('welcome.html', post = post)

@postsAPI.route('/posting', methods=['GET', 'POST'])
def posting():
    if request.method == 'GET':
        if 'userEmail' in session:
            post = posts.postValidation()
            info = session['userEmail'].split('@')
            return render_template('welcome.html', info = info[0], post = post)
        else:
            post = posts.postValidation()
            return render_template('welcome.html', post = post)

    if request.method == 'POST':
        if 'userEmail' in session:
            posts.postCreate(request.form.to_dict(flat='true'))
            post = posts.postValidation()
            info = session['userEmail'].split('@')
            return render_template('welcome.html', info = info[0], post = post)
        else:
            post = posts.postValidation()
            return render_template('welcome.html', post = post)

@postsAPI.route('/postview', methods=['GET'])
def postview():
    if 'userEmail' in session:
        info = session['userEmail'].split('@')
        post = posts.postValidation()
        return render_template('postview.html', info = info[0], post = post)
    else:
        post = posts.postValidation()
        return render_template('welcome.html', post = post)

