from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Department(db.Model):
    '''
        Develop of data model based on csv files for departments
    '''
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Department {self.department}>'

class Job(db.Model):
    '''
        Develop of data model based on csv files for jobs
    '''
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Job {self.job}>'

class Employee(db.Model):
    '''
        Develop of data model based on csv files for employees
    '''
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.String(100), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=True)
    partition_column = db.Column(db.String(100), nullable=False)

    department = db.relationship('Department', backref=db.backref('employees', lazy=True))
    job = db.relationship('Job', backref=db.backref('employees', lazy=True))

    def __repr__(self):
        return f'<Employee {self.name}>'
