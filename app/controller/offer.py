import os
import random
from flask import Blueprint, render_template, request, Flask, url_for, app, flash
from werkzeug.utils import redirect
from app.models.base import db
from app.models.comoffer import ComOffer
from app.models.offer import Offer
import app.controller.user as user
from faker import Faker
from sqlalchemy import or_,and_,all_,any_,func
from sqlalchemy import update

from app.models.program import Program
from app.models.researchoffer import ResearchOffer
from app.models.tcoffer import TaughtOffer
from app.models.uicer import UICer
from app.models.university import University

offerBP = Blueprint('offer',__name__)
f = Faker()
@offerBP.route('', methods=['GET'])
def add_offer(name, universityname,GPAlow,GPAupper):
    with db.auto_commit():
        
            offer = Offer(name, universityname,GPAlow,GPAupper)
            # 数据库的insert操作
            db.session.add(offer)
    return 'hello offer'

@offerBP.route('/test', methods=['GET'])
def test_offer():
    with db.auto_commit():
        for i in range(20):
            offer = Offer(f.year(), f.pyfloat(left_digits=1,right_digits=2,positive=True,min_value=0.1, max_value=4.0),f.random_int(min=0,max=1),i+1,i+1,f.word(),'/offerImages/offer'+str(i+1)+'.png')
            # 数据库的insert操作
            db.session.add(offer)
    return 'hello program'
@offerBP.route('/verify', methods=['GET'])
def verify():
#sql获取reality，1为real
    return 0
    # 未完成

def updateProgram(GPA,programname, universityname):

    # Every time adding an offer, ststem automatically check the university and the program to obtain the max and min GPA
    # and then update the Program table in DB

    result_maxGPA = db.session.query(func.max(Offer.GPA)).filter(Offer.universityname == universityname, Offer.programe == programname).first()
    result_minGPA = db.session.query(func.min(Offer.GPA)).filter(Offer.universityname == universityname, Offer.programe == programname).first()


    # GPAmin = int(result_minGPA[0])
    print("Max ", result_maxGPA[0])
    print("Min: ", result_minGPA[0])
    GPAmax = float(result_maxGPA[0])
    GPAmin = float(result_minGPA[0])
    ## Firstly check if the program is already in DB
    ## if in, update the min and max GPA
    ## if not in, add this program

    result = Program.query.filter(and_(Program.name == programname)).first()
    if result:
        try:
            Program.query.filter_by(name=programname).update({Program.GPAupper: GPAmax})
            Program.query.filter_by(name=programname).update({Program.GPAlow: GPAmin})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    else:
        result_university = University.query.filter(and_(University.name == universityname)).first()
        university_id = result_university.id
        newprogram = Program(programname, universityname,GPAmin,GPAmax,university_id)
        db.session.add(newprogram)
        db.session.commit()


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
UPLOAD_FOLDER = basedir + '\offerImages'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'])
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

offerList = []

@offerBP.route('/reportoffer', methods=['GET','POST'])
def reportoffer():
    if request.method == 'GET':
        return render_template('reportoffer.html')
    else:
        offertype = request.form.get('offertype')
        print("ofer",offertype)
        print("ofer", type(offertype))
        year = request.form.get('year')
        college = request.form.get('college')
        programe = request.form.get('programe')
        imgfile = request.files['image']
        supervisor = request.form.get('supervisor')
        researchtopic = request.form.get('topic')
        paper = request.form.get('paper')
        research = request.form.get('research')
        title = request.form.get('jobtitle')
        companyname = request.form.get('companyname')
        companycountry = request.form.get('companycountry')
        qualification = request.form.get('qualification')

        findUniversity = University.query.filter(and_(University.name == college)).first()

        print(year, college, programe)
        result = UICer.query.filter(and_(UICer.email == user.currentUser)).first()
        if result:
            print(result.id)
            uicer_id = result.id
            GPA = result.GPA

        if imgfile and allowed_file(imgfile.filename):
            filename = imgfile.filename
            print("file name:",filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            photocopy = '../offerImages/' + filename
            print(file_path,'ulr',photocopy)
            imgfile.save(os.path.join(UPLOAD_FOLDER, filename))
            global offerList
            offerList.clear()
            if offertype == '1':
                # taught
                print("ta",year, GPA, 1, uicer_id, college, programe, photocopy)
                if findUniversity:
                    ## if find university name in our DB, add offer derictly
                    with db.auto_commit():
                        taughtoffer = TaughtOffer(year, GPA, 1, uicer_id, college, programe, photocopy)
                        db.session.add(taughtoffer)
                    updateProgram(GPA, programe, college)
                    flash("Add taught offer successfully!")
                else:
                    ## if Univesity is not in our DB, go to another page for dtail and add offer
                    for i in [year, GPA, 1, uicer_id, college, programe, photocopy]:
                        offerList.append(i)
                    return redirect(url_for('offer.offerUniversityDetail'))
            elif offertype == '2':
                # research
                paper = int(paper)
                research = int(research)
                print("re",year, GPA, 1, uicer_id, college, programe, photocopy,supervisor,researchtopic,paper,research)

                if findUniversity:
                    with db.auto_commit():
                        researchoffer = ResearchOffer(year, GPA, 1, uicer_id, college, programe, photocopy, supervisor,
                                                      researchtopic, paper, research)
                        db.session.add(researchoffer)
                    updateProgram(GPA, programe, college)
                    flash("Add research offer successfully!")
                else:
                    for i in [year, GPA, 1, uicer_id, college, programe, photocopy, supervisor, researchtopic, paper,
                              research]:
                        offerList.append(i)
                    ## if Univesity is not in our DB, go to another page for dtail and add offer
                    return redirect(url_for('offer.offerUniversityDetail'))
            else:
                # company
                print("co",year, GPA, 1, uicer_id, college, programe, photocopy,title,companyname,companycountry,qualification)
                with db.auto_commit():
                    companyoffer = ComOffer(year, GPA, 1, uicer_id, college, programe, photocopy,title,companyname,companycountry,qualification)
                    db.session.add(companyoffer)
                flash("Add company offer successfully!")


            #imgfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',filename=filename))
        return redirect(url_for('offer.reportoffer'))



@offerBP.route('/offerUniversityDetail', methods=['GET','POST'])
def offerUniversityDetail():
    if request.method == 'GET':
        return render_template('offerUniversityDetail.html')
    else:
        global offerList
        college = request.form.get('college')
        collegeCity = request.form.get('collegecity')

        print(offerList)
        print(len(offerList))
        offerLen = len(offerList)
        #if length of offerList is 7, the offer is taught offer,
        # if length is 11 the offer is research offer

        if offerLen == 7:
            # Since the uiniversity is not in our DB, we add a new university
            with db.auto_commit():
                Newuniversity = University(college, "", collegeCity)
                db.session.add(Newuniversity)

            with db.auto_commit():
                taughtoffer = TaughtOffer(offerList[0], offerList[1], offerList[2], offerList[3], offerList[4], offerList[5], offerList[6])
                db.session.add(taughtoffer)
            updateProgram(offerList[1], offerList[5], offerList[4])
            flash("Add taught offer successfully!")
        else:
            # Since the uiniversity is not in our DB, we add a new university
            with db.auto_commit():
                Newuniversity = University(college, "", collegeCity)
                db.session.add(Newuniversity)

            with db.auto_commit():
                researchoffer = ResearchOffer(offerList[0], offerList[1], offerList[2], offerList[3], offerList[4], offerList[5], offerList[6], offerList[7], offerList[8], offerList[9], offerList[10])
                db.session.add(researchoffer)
            updateProgram(offerList[1], offerList[5], offerList[4])
            flash("Add research offer successfully!")

    return redirect(url_for('offer.offerUniversityDetail'))
