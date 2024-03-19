import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError

app=Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#db.init_app(app)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    age = db.Column(db.Integer)
    time = db.Column(db.DateTime(timezone=True), server_default = func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f"<student {self.firstname}>"

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)
@app.route('/<int:student_id>')
def stud(student_id):
    student_for_stud = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student_for_stud)

@app.route('/create', methods=('POST','GET'))
def create():
    if request.method=='POST':
        firstname1=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        age=int(request.form['age'])
        bio=request.form['bio']
        # Attempt to add the student to the database
        try:
            firstname1 = Student(firstname=firstname1, lastname=lastname, email=email, age=age, bio=bio)
            db.session.add(firstname1)
            db.session.commit()
            return redirect(url_for('index'))
        except IntegrityError:
            # Rollback the session to prevent partially completed transactions
            db.session.rollback()
            # Return a message to the user indicating that the email is already taken
            return "Email already exists. Please use a different email."
    return render_template('create.html')

@app.route('/<int:student_id>/edit', methods=('POST', 'GET'))
def edit(student_id):
    student_for_edit = Student.query.get_or_404(student_id)
    if request.method=='POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        age=int(request.form['age'])
        bio=request.form['bio']
        student_for_edit.firstname=firstname
        student_for_edit.lastname=lastname
        student_for_edit.email=email
        student_for_edit.age=age
        student_for_edit.bio=bio
        db.session.add(student_for_edit)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html', student=student_for_edit)

@app.post('/<int:student_id>/delete')
def delete(student_id):
    student_for_delete = Student.query.get_or_404(student_id)
    db.session.delete(student_for_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)
