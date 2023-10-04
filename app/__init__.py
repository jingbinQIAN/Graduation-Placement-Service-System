from flask import Flask, session
from app.controller import user, knowledge, offer, report, alumni
from flask_session import Session
import os


def register_blueprints(app):
    app.register_blueprint(user.userBP, url_prefix='/user')
    app.register_blueprint(knowledge.knowledgeBP, url_prefix='/knowledge')
    app.register_blueprint(offer.offerBP, url_prefix='/offer')
    app.register_blueprint(report.reportBP, url_prefix='/report')
    app.register_blueprint(alumni.alumniBP, url_prefix='/alumni')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    register_blueprints(app)
    register_plugin(app)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = os.urandom(24)
    Session(app)
    return app
