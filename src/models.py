from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class To_do(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(150), primary_key=True )
    done = db.Column(db.Boolean)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    to_do_id= db.Column(Integer, ForeignKey('to_do.id'))
    label_r=relationship('To_do')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
            return {
                "id": self.id,
                "username": self.username,
                # do not serialize the password, its a security breach
        }

    def addUser():
        user1 = User()
        user1.username="Luigi"
        db.session.add(user1)
        db.session.commit()   
    

