from flask import Blueprint, render_template, request, jsonify, url_for, flash
from app.models.base import db
from app.models.alumni import Alumni
from werkzeug.utils import redirect

alumniBP = Blueprint('alumni',__name__)

@alumniBP.route('/add',methods=['GET','POST'])
def add_Alumni():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        college = request.form.get('college')
        GPA = request.form.get('GPA')
        status = request.form.get('type')
        new_password = request.form.get('newpwd')
        ver_password = request.form.get('verpwd')
        print(name, email, age, college, GPA, status, new_password, ver_password)
        print(type(status))
        if new_password == ver_password:
            if status == "2":
                with db.auto_commit():
                    alumni = Alumni(name, age, college, email, new_password, GPA, 2)
                    db.session.add(alumni)
                flash("Register successfully!")
        else:
            flash("New password and verify password are not the same!", category="error")

        return redirect(url_for('user.register'))
