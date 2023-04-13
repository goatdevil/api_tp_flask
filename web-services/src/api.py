from flask import  Flask,jsonify
from flask_sqlalchemy import   SQLAlchemy
from datetime import datetime
from faker import Faker
import random


app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://root:root@localhost:5432/store"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db= SQLAlchemy(app)

@app.route("/user")
def get_user():
    result=User.query.all()
    data=[]
    for object in result:
        user = {
            "id":object.id,
            "firstname":object.firstname,
            "lastname":object.lastname,
            "age":object.age,
            "email":object.email,
            "job":object.job

        }
        data.append(user)
    return jsonify(data)




class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String(100))
    lastname=db.Column(db.String(100))
    age=db.Column(db.Integer())
    email=db.Column(db.String(200))
    job=db.Column(db.String(100))
    application =db.relationship('Application')

    def __init__(self,firstname,lastname,age,email,job):
        self.firstname =firstname
        self.lastname=lastname
        self.age=age
        self.email=email
        self.job=job

class Application(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    appname =db.Column(db.String(100))
    username=db.Column(db.String(100))
    lastconnexion=db.Column(db.TIMESTAMP(timezone=True))
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self,appname,username,lastconnexion):
        self.appname=appname
        self.username=username
        self.lastconnexion=lastconnexion

def populate_tables():
    fake = Faker()
    applications=["Facebook","Instagram","Youtube","Twitter","Airbnb"]
    for n in range(100):
        firstname=fake.first_name()
        lastname=fake.last_name()
        age=random.randrange(18,50)
        email=fake.email()
        job=fake.job()
        user=User(firstname,lastname,age,email,job)

        apps_names=[random.choice(applications) for n in range(1,random.randrange(1,5))]
        for app_name in apps_names:
            username=fake.user_name()
            lastconnection=datetime.now()
            new_app=Application(app_name,username,lastconnection)
            user.application.append(new_app)

        with app.app_context():
            db.session.add(user)
            db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
    populate_tables()

    app.run(host='0.0.0.0',port=8081,debug=True)