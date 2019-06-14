from flask import Blueprint, request, render_template, session, redirect, url_for
from .db import connect_mongo, postsDAO, profileDAO
import time

def dict_merge(x, y):
    return {**x, **y}

db_connection = connect_mongo.ConnectDB().db
posts = postsDAO.Posts(db_connection)
profile = profileDAO.Profile(db_connection)

postsAPI = Blueprint('postsAPI', __name__, template_folder='templates')

@postsAPI.route('/', methods=['GET'])
def base():
    if request.method == 'GET':
        if 'userEmail' in session:
            post = posts.getAllposts()
            postcount = posts.getPostsCount()
            pro = profile.profileValidation()
            info = session['userEmail'].split('@')
            return render_template('welcome.html', info = info[0], post = post, postcount = postcount, profile = pro)
        else:
            post = posts.getAllposts()
            postcount = posts.getPostsCount()
            pro = profile.profileValidation()
            return render_template('welcome.html', post = post, postcount = postcount, profile = pro)

@postsAPI.route('/posting', methods=['GET', 'POST'])
def posting():
    if request.method == 'GET':
        if 'userEmail' in session and session['userEmail'] == 'admin@admin':
            info = session['userEmail'].split('@')
            return render_template('post.html', info = info[0])
        else:
            return redirect(url_for('postsAPI.base'))

    if request.method == 'POST':
        if 'userEmail' in session and session['userEmail'] == 'admin@admin':
            if request.form['postTitle'] != '' and request.form['postContent'] != '':
                now = time.strftime("%Y-%m-%d %H:%M")
                obj_id = posts.postCreate(dict_merge({"author":session['userEmail'], "date":now}, request.form.to_dict(flat=True)))
                return redirect(url_for('postsAPI.base'))
            else:
                return redirect(url_for('postsAPI.posting'))
        else:
            return redirect(url_for('postsAPI.base'))

@postsAPI.route('/post/update', methods=['POST'])
def postUpdate():
    if 'userEmail' in session and session['userEmail'] == 'admin@admin':
        posts.postUpdate(request.form.to_dict(flat=True))
        return redirect(url_for('postsAPI.postMore',postTitle = request.form['postTitle'], postContent = request.form['postContent']))
    else:
        return redirect(url_for('postsAPI.base'))
      
@postsAPI.route('/post/delete', methods=['POST'])
def postDelete():
    if 'userEmail' in session and session['userEmail'] == 'admin@admin':
        posts.postDelete(request.form.to_dict(flat=True)["obj_id"])
        return redirect(url_for('postsAPI.base'))
    else:
        return redirect(url_for('postsAPI.base'))

@postsAPI.route('/postmore/<string:postTitle>/<string:postContent>', methods=['GET'])
def postMore(postTitle, postContent):
    if 'userEmail' in session:
        post = posts.getOneposts(postTitle, postContent)
        info = session['userEmail'].split('@')
        return render_template('postmore.html', post = post, info = info[0])
    else:
        return redirect(url_for('postsAPI.base'))
