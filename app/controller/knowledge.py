from flask import Blueprint, render_template, request, jsonify, url_for, flash
from werkzeug.utils import redirect
from app.models.base import db
from app.models.knowledge import Knowledge
from app.models.uicer import UICer
from app.models.program import Program
import app.controller.user as user
from faker import Faker
from sqlalchemy import or_, and_, all_, any_, func
import random

from app.models.university import University

f = Faker()
knowledgeBP = Blueprint('knowledge', __name__)


def getGraduateYear(email):
    return int(ord(email[0]) - ord('p') + 2023)


@knowledgeBP.route('/viewKnowledgePoint', methods=['GET', 'POST'])
def viewKnowledgePoint():
    if request.method == 'GET':
        return render_template('viewKnowledgePoint.html')
    else:
        type = request.form.get('knowledgeType')
        university = request.form.get('search1')
        program = request.form.get('search2')
        print(type)
        print(university)
        print(program)
        if type == "University":
            result = db.session.query(Knowledge.universityname, Knowledge.programname, Knowledge.alumniname,
                                      Knowledge.comment, Knowledge.year_visible, Knowledge.gender_visible,
                                      Knowledge.name_visible, Knowledge.alu_id, Knowledge.coursename).filter(
                and_(Knowledge.universityname == university)).all()

            if result:
                show_knowledge_point_detail(result)
            else:
                flash("Does not have this university!")
        if type == "Program":
            result = db.session.query(Knowledge.universityname, Knowledge.programname, Knowledge.alumniname,
                                      Knowledge.comment, Knowledge.year_visible, Knowledge.gender_visible,
                                      Knowledge.name_visible, Knowledge.alu_id, Knowledge.coursename).filter(
                and_(Knowledge.programname == program)).all()
            if result:
                show_knowledge_point_detail(result)
            else:
                flash("Does not have this program!")

    return redirect(url_for('knowledge.viewKnowledgePoint'))


@knowledgeBP.route('/provideKLPoint', methods=['GET', 'POST'])
def provideKLPoint():
    if request.method == 'GET':
        return render_template('provideKLPoint.html')
    else:

        programName = request.form.get('program')
        courseName = request.form.get('courseName')
        collegeName = request.form.get('college')
        comment = request.form.get('comment')
        year_visible = request.form.get('year_visible')
        name_visible = request.form.get('name_visible')
        gender_visible = request.form.get('gender_visible')

        if year_visible == "1":
            year_visible = int(year_visible)
        else:
            year_visible = 0

        if name_visible == "1":
            name_visible = int(name_visible)
        else:
            name_visible = 0

        if gender_visible == "1":
            gender_visible = int(gender_visible)
        else:
            gender_visible = 0

        find_user = UICer.query.filter(and_(UICer.email == user.currentUser)).first()
        alumni_id = find_user.id
        alumni_name = find_user.name

        get_program_id = Program.query.filter(
            and_(Program.name == programName, Program.universityname == collegeName)).first()

        if get_program_id:
            program_id = get_program_id.id
        else:
            program_id = random.randint(1, 6)

        print(alumni_name, programName, courseName, collegeName, comment)
        with db.auto_commit():
            kp = Knowledge(alumni_name, courseName, collegeName, programName, alumni_id, program_id, comment,
                           year_visible, gender_visible, name_visible)
            db.session.add(kp)
        flash("Share successfully!")
        return redirect(url_for('knowledge.provideKLPoint'))


def show_knowledge_point_detail(result):
    i = 1
    for x in result:
        genderAlu = db.session.query(UICer.gender, UICer.email).filter(and_(UICer.id == x[7])).first()
        print(genderAlu.gender)
        graduateYear = getGraduateYear(genderAlu.email)
        print(graduateYear)
        if x[4] == 0 and x[5] == 0 and x[6] == 0:
            showlist = x[0] + "     " + str(
                x[1]) + "      anonymous" + "    Graduate Year: invisible "
        if x[4] == 0 and x[5] == 0 and x[6] == 1:
            showlist = x[0] + "   " + str(
                x[1]) + "       " + str(x[2]) + "     Graduate Year: invisible " + "  Comment:      " + str(
                x[3])
        if x[4] == 0 and x[5] == 1 and x[6] == 0:
            showlist = x[0] + "     " + str(
                x[1]) + "       anonymous       " + str(
                genderAlu.gender) + "       Graduate Year: invisible "
        if x[4] == 0 and x[5] == 1 and x[6] == 1:
            showlist = x[0] + "     " + str(
                x[1]) + "       " + str(x[2]) + "       " + str(
                genderAlu.gender) + "       Graduate Year: invisible "
        if x[4] == 1 and x[5] == 0 and x[6] == 0:
            showlist = x[0] + "     " + str(
                x[1]) + "       anonymous" + "      Graduate Year: " + str(
                graduateYear)
        if x[4] == 1 and x[5] == 0 and x[6] == 1:
            showlist = x[0] + "     " + str(
                x[1]) + "       " + str(x[2]) + "       Graduate Year: " + str(
                graduateYear)
        if x[4] == 1 and x[5] == 1 and x[6] == 0:
            showlist = x[0] + "     " + str(
                x[1]) + "       anonymous       " + str(
                genderAlu.gender) + "       Graduate Year: " + str(graduateYear)
        if x[4] == 1 and x[5] == 1 and x[6] == 1:
            showlist = x[0] + "     " + str(
                x[1]) + "       " + str(x[2]) + "       " + str(
                genderAlu.gender) + "       Graduate Year: " + str(graduateYear)
        comment = "Comment:     " + str(x[3])
        flash(str(i))
        flash(showlist)
        flash(str(x[8]))
        flash(comment)
        i += 1
