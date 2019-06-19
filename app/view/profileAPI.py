from flask import Blueprint, request, render_template, session, redirect, url_for
from .db import connect_mongo, profileDAO
from werkzeug import secure_filename

def dict_merge(x, y):
    return {**x, **y}

db_connection = connect_mongo.ConnectDB().db
profile = profileDAO.Profile(db_connection)

profileAPI = Blueprint('profileAPI', __name__, template_folder='templates')

@profileAPI.route('/')
@profileAPI.route('/profile', methods=['GET', 'POST'])
def profileUpdate():
        if request.method == 'GET':
                if 'userEmail' in session and session['userEmail'] == 'admin@admin':
                        pro = profile.profileValidation()
                        info = session['userEmail'].split('@')
                        return render_template('profile.html', info = info[0], profile = pro)
                else:
                        return redirect(url_for('postsAPI.base'))

        if request.method == 'POST':
                if 'userEmail' in session and session['userEmail'] == 'admin@admin':
                        f = request.files['file']
                        if f.filename == '':
                                profile.profileUpdate('', request.form.to_dict(flat='true'))
                                return redirect(url_for('postsAPI.base'))
                        else:
                                f.save("./static/img/" + secure_filename(f.filename))
                                profile.profileUpdate(f.filename,request.form.to_dict(flat='true'))
                                return redirect(url_for('postsAPI.base'))
                else:
                        return redirect(url_for('postsAPI.base'))

