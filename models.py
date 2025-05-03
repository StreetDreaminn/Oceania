from flask_login import UserMixin
from . import db

class Oceania_Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)