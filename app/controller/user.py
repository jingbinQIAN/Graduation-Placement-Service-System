from flask import Blueprint, render_template, request, jsonify, url_for, flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
import datetime
from app.models.base import db
from app.models.uicer import UICer
from app.models.alumni import Alumni
from app.models.university import University
from app.models.program import Program
from sqlalchemy import or_,and_,all_,any_
from sqlalchemy import update

userBP = Blueprint('user',__name__)

currentUser = ""


@userBP.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Sample Login', header='Sample Case')
    else:

        email = request.form.get("email")
        _password = request.form.get('password')

        global currentUser
        currentUser = email

        print(email, _password)
        if not all([email, _password]):
            # if any empty return error result
            return jsonify(code=1001, message='Parameter incomplete!')

        result = UICer.query.filter(and_(UICer.email == email, UICer._password == _password)).first()
        # tr = TimetableRecord.query.filter(and_(TimetableRecord.tid==tid, TimetableRecord.day == day,TimetableRecord.status!=2)).first()
        # print(result .jsonstr())

        if result:
            print(result.email)
            print(result._password)

            # return jsonify(code=0, message="Success!")
            return redirect(url_for('user.userCase'))
            # return render_template('success.html',title='Success Login')
        else:
            flash("Not a correct email or password!", category="error")
            # return jsonify(code=1001, message="Not correct email or password!")
            return render_template('login.html', title='Sample Login', header='Sample Case')




@userBP.route('/changePwd',methods=['GET','POST'])
def changePwd():
    global currentUser

    if request.method == 'GET':
        return render_template('changePwd.html')
    else:
        old_password = request.form.get('oldpwd')
        new_password = request.form.get('newpwd')
        ver_password = request.form.get('verpwd')

        result = UICer.query.filter(and_(UICer.email == currentUser,UICer._password == old_password)).first()

        if result:
            if new_password == ver_password:
                UICer.query.filter_by(email=currentUser).update({UICer._password : new_password})
                db.session.commit()
                flash("Update new password successfully!")
            else:
                flash("New password and verify password are not the same!", category="error")
        else:
            flash("Wrong old password!", category="error")

        return redirect(url_for('user.changePwd'))

@userBP.route('/userCase',methods=['GET','POST'])
def userCase():
    global currentUser
    print(currentUser)
    result = UICer.query.filter(and_(UICer.email == currentUser)).first()
    today = datetime.datetime.today()
    year = today.year
    currentLetter = 'o'
    currentLetter = ord(currentLetter) + (int(year)-2023)
    currentLetter = chr(currentLetter)
    print(currentLetter)
    if result.status == 1:
        if currentUser[0] < currentLetter:
            try:
                UICer.query.filter_by(email=currentUser).update({UICer.status: 2})
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
            return render_template('userCase_Alumni.html')
        else:
            return render_template('userCase_UICer.html')
    if result.status == 2:
        return render_template('userCase_Alumni.html')
    if result.status == 3:
        return render_template('userCase_Admin.html')
    else:
        flash("You should login again!")
        return render_template('login.html')

@userBP.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        age = request.form.get('age')
        college = request.form.get('college')
        GPA = request.form.get('GPA')
        status = request.form.get('usertype')
        new_password = request.form.get('newpwd')
        ver_password = request.form.get('verpwd')
        gender = request.form.get('gender')
        print(name, email, age, college, GPA, status, new_password, ver_password)
        print(type(status))
        if gender == "":
            flash("You should select a gender!")
            return redirect(url_for('user.register'))

        find_email = UICer.query.filter(and_(UICer.email == email)).first()
        if find_email:
            flash("This email has already been registered.")
            return redirect(url_for('user.register'))

        if new_password == ver_password:
            if status == "1":
                with db.auto_commit():
                    uicer = UICer(name, age, college, email, new_password, GPA, 1,gender)
                    db.session.add(uicer)
                flash("Register successfully!")
            if status == "2":
                with db.auto_commit():
                    alumni = Alumni(name, age, college, email, new_password, GPA, 2,gender)
                    db.session.add(alumni)
                flash("Register successfully!")
        else:
            flash("New password and verify password are not the same!", category="error")

        return redirect(url_for('user.register'))


@userBP.route('/search', methods=['GET', 'POST'])
def search():
    global currentUser

    if request.method == 'GET':
        return render_template('search.html')
    else:
        select = request.form.get('select1')
        print(select)
        if (select == "gpa"):
            gpa1 = request.form.get('gpa')
            print(gpa1)
            result = Program.query.filter(Program.GPAlow <= gpa1).all()
            if result:
                return render_template('searchresult.html', content=result)
            else:
                flash("Error!", category="error")
        if (select == "pname"):
            pname = request.form.get('pname')
            result = Program.query.filter(Program.name == pname).order_by(Program.name).all()
            # flash(result)
            if result:
                # flash("good!")
                return render_template('searchresult2.html', content=result)
            else:
                flash("Error!", category="error")

        return redirect(url_for('user.search'))
