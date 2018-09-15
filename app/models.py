from flask_login import UserMixin
from . import db



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True) 
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'users',lazy="dynamic")

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    def save_comment(self):
        db.session.add(self)
        db.session.commit()