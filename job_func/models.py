from datetime import datetime
from job_func import db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_keyword = db.Column(db.String(100), nullable=False)
    search_location = db.Column(db.String(100), nullable=False)
    search_radius = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.String(100), nullable=False)
    valid_through = db.Column(db.String(100), nullable=False)
    hiring_organisation = db.Column(db.String(100), nullable=False)
    hiring_city = db.Column(db.String(100), nullable=False)
    hiring_region = db.Column(db.String(100), nullable=False)
    hiring_contact = db.Column(db.String(100), nullable=False)
    hiring_reference = db.Column(db.String(100), nullable=False)
    job_id = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    application_stages = db.relationship('ApplicationStage', backref='job', lazy=True)

    def __repr__(self):
        return f"Job('{self.title}', '{self.date_posted}', '{self.valid_through}')"


class ApplicationStage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    date_applied = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    note = db.Column(db.Text, nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

    def __repr__(self):
        return f"ApplicationStage('{self.status}', '{self.date_applied}')"
