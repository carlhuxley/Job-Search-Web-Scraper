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
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_posted = db.Column(db.String(100), nullable=False)
    valid_through = db.Column(db.String(100), nullable=False)
    date_applied = db.Column(db.DateTime, nullable=True)
    hiring_organisation = db.Column(db.String(100), nullable=False)
    hiring_city = db.Column(db.String(100), nullable=False)
    hiring_region = db.Column(db.String(100), nullable=False)
    hiring_contact = db.Column(db.String(100), nullable=False)
    hiring_reference = db.Column(db.String(100), nullable=False)
    job_id = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    application_stages = db.relationship('Stage',
                                         backref='job', lazy=True)

    def __repr__(self):
        return f"Job('{self.title}', '{self.date_posted}', '{self.valid_through}')"


class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(25), nullable=True)
    note = db.Column(db.Text, nullable=True)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    status_choices = db.relationship('Choice',
                                         backref='stage', lazy=True)


    def __repr__(self):
        return f"Stage('{self.status}', '{self.job_id}')"


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    extra = db.Column(db.String(50))
    stage_id = db.Column(db.Integer, db.ForeignKey('stage.id'), nullable=True)

    def __repr__(self):
        return f"Choice('{self.name}')"
