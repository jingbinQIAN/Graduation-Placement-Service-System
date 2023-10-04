from flask import Blueprint, render_template, request, jsonify, url_for, flash
from app.models.base import db
from app.models.report import Report
from app.models.comoffer import ComOffer
from app.models.offer import Offer
import app.controller.user as user
from werkzeug.utils import redirect
from sqlalchemy import or_,and_,all_,any_,func
from faker import Faker
reportBP = Blueprint('report',__name__)
f=Faker()

@reportBP.route('/test', methods=['GET'])
def add_report():
    with db.auto_commit():
        for i in range(20):
            report = Report(f.year(),f.random_int(min=1,max=10))
            # 数据库的insert操作
            db.session.add(report)
    return 'hello report'



@reportBP.route('/export',methods=['GET','POST'])
def export():
    if request.method == 'GET':
        return render_template('report.html')
    else:
        year = request.form.get('years')
        if year == "":
            flash("You should select a year!")
        else:
            year = int(year)
            result = Report.query.filter(and_(Report.year == year)).first()
            print(year)
            if result:
                message = "The total offers of the year " + str(year) + " is: " + str(result.totaloffers)
                flash(message)
                university_offer_count = db.session.query(Offer).filter(Offer.year == year, Offer.universityname != "").count()
                company_offer_count = db.session.query(Offer).filter(Offer.year == year, Offer.universityname == "").count()
                flash("University Offer: "+str(university_offer_count)+"        Company Offer: "+str(company_offer_count))
                flash("University Offer: ")
                result_more_than2 = db.session.query(Offer.universityname, func.max(Offer.GPA), func.min(Offer.GPA)).filter(Offer.year == year, Offer.universityname != "").group_by(Offer.universityname).having(func.count(Offer.universityname) > 2).all()
                result_less_than2 = db.session.query(Offer.universityname, func.max(Offer.GPA), func.min(Offer.GPA)).filter(Offer.year == year, Offer.universityname != "").group_by(Offer.universityname).having(func.count(Offer.universityname) <= 2).all()
                # Randomly impose the minimum range over the actual GPA of the student
                new_list = [(x[0], x[1]+0.02, x[2]) for x in result_less_than2]
                full_list = result_more_than2 + new_list
                show_list = ["University Name: "+x[0]+"  Max GPA: "+str(x[1])+"  Min GPA: "+str(x[2]) for x in full_list]
                for info in show_list:
                    flash(info)
                flash("Company Offer: ")
                company_result = db.session.query(ComOffer.companyname).filter(Offer.year == year, Offer.universityname == "").group_by(ComOffer.companyname).all()
                # Randomly impose the minimum range over the actual GPA of the student
                company_name_list = [x[0] for x in company_result]
                company_count_list = []
                for i in company_name_list:
                    count = db.session.query(ComOffer).filter(ComOffer.companyname == str(i)).count()
                    company_count_list.append(count)

                company_list = [list(t) for t in zip(company_name_list, company_count_list)]
                company_show = ["Company Name: " + str(x[0]) + "     Offer Number: "+str(x[1]) for x in company_list]
                for info in company_show:
                    flash(info)
            else:
                flash("This year has no offer.")
    return redirect(url_for('report.export'))

@reportBP.route('/generateReport',methods=['GET','POST'])
def generateReport():
    if request.method == 'GET':
        return render_template('generateReport.html')
    else:
        year = request.form.get('years')
        if year == "":
            flash("You should select a year!")
        else:
            year = int(year)
            print(year)
            count = db.session.query(Offer).filter(Offer.year == year).count()
            print(count)
            print(type(count))
            if count != 0:
                result = Report.query.filter(and_(Report.year == year)).first()
                print(result)
                if result:
                    try:
                        Report.query.filter_by(year=year).update({Report.totaloffers: count})
                        db.session.commit()
                    except Exception as e:
                        db.session.rollback()
                        raise e
                else:
                    print("test")
                    count = db.session.query(Offer).filter(Offer.year == year).count()
                    print(year)
                    print(count)
                    report = Report(year, count)
                    db.session.add(report)
                    db.session.commit()
                flash("Generate report successfully!")
            else:
                flash("This year has no offer.")

    return redirect(url_for('report.generateReport'))
