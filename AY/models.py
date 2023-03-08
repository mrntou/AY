from flask_login import UserMixin
from AY import db, app, login_manager
from datetime import datetime



@login_manager.user_loader
def load_admin(admin_id):
    return Admin.query.get(admin_id)

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(280))


    def check_password(self, password):
        if self.password == password:
            return True
        
    def __repr__(self):
        return self.username




class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    branch = db.Column(db.String(80))
    specialty = db.Column(db.String(80))
    # Database Relationships by id
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    speciality_id = db.Column(db.Integer, db.ForeignKey('speciality.id'), nullable=False)
    # One to One Relationship
    # permits = db.relationship('Permit', backref='employee', uselist=False)


class Permit(db.Column):
    __tablename__ = 'permit'
    id = db.Column(db.Integer, primary_key=True)
    # Κανονική άδεια
    normal = db.Column(db.Integer, default=0)
    # Παρακουλούθησης σχολικη΄ς επίδοσης
    pse = db.Column(db.Integer, default=0)
    # Αναρρωτική
    an = db.Column(db.Integer, default=0)
    # Ειδική Αναρρωτική
    ei_an = db.Column(db.Integer, default=0)
    # Ασθένειες τέκνου
    as_tek = db.Column(db.Integer, default=0)
    # Αιμοδοτική
    aimo = db.Column(db.Integer, default=0)
    # Γυναικολογική
    gyne = db.Column(db.Integer, default=0)
    # Γάμου
    gamo = db.Column(db.Integer, default=0)
    # Ειδική άδεια λόγου θανάτου
    than = db.Column(db.Integer, default=0)
    # Πατρότητας
    pat = db.Column(db.Integer, default=0)
    # Μητρότητας
    mht = db.Column(db.Integer, default=0)
    # Ειδική άδεια εκλογικού δικαιώματος
    eklo = db.Column(db.Integer, default=0)
    # Ειδικά άδεια δικστηρίου
    dika = db.Column(db.Integer, default=0)
    # ΑμεΑ
    amea = db.Column(db.Integer, default=0)
    # Αιμοληψίας    
    aima = db.Column(db.Integer, default=0)

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)


class Leave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permit_name = db.Column(db.String(80))
    dates = db.relationship('Date', backref='event')


class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('leave.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)



class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    employees = db.relationship('Employee', backref='department', lazy=True)


class Speciality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    employees = db.relationship('Employee', backref='speciality', lazy=True)
    


    


