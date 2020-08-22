from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class To_do(db.Model):
    id= db.Column(db.Integer, primary_key=True, unique=True) 
    label = db.Column(db.String(150), nullable=False) 
    done = db.Column(db.Boolean)

    def __repr__to(self):
            return '<To_do %r>' % self.username

    def serialize(self):
            return {
                "id": self.id,
                "label": self.label,
                "done": self.done
                # do not serialize the password, its a security breach
        }

    
    def add_to_do(data):
        for i in range(len(data)):
            to_do=To_do()
            to_do.label=data[i]["label"]
            to_do.done=data[i]["done"]
            #     todo_list = list(map(lambda item: item.serialize(),data))
            #     print(todo_list)
            db.session.add(to_do)
            db.session.commit()

    @classmethod
    def get_to_do(Task):
        tasks = Task.query.all()
        todo_list = list(map(lambda task: task.serialize(),tasks))
        return todo_list
    
    def delete_to_do(Task):
        tasks = Task.query.all()
        todo_list = list(map(lambda task: task.serialize(),tasks))
        return todo_list
        



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
    

