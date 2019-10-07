from datetime import datetime
from flask import Flask
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from job_search import job_search

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

db.create_all()

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

@app.route('/')
def search():
    return render_template('search_jobs.html')


@app.route('/get_jobs', methods=['POST', 'GET'])
def get_jobs():
    if request.method == 'POST':
        search = request.form
        keyword = search["Keyword"]
        location = search["Location"]
        radius = search["Radius"]
        posted = search["Posted"]
        jobs = job_search(keyword, location, radius, posted)

        for job in jobs:
            job = Job(**job)
            """
            job = Job(search_keyword=job['search_keyword'],
                    search_location=job['search_location'],
                    search_radius=job['search_radius'],
                    title=job['title'],
                    salary=job['salary'],
                    job_type=job['job_type'],
                    link=job['link'],
                    date_posted=job['date_posted'],
                    valid_through=job['valid_through'],
                    hiring_organisation=job['hiring_organisation'],
                    hiring_city=job['hiring_city'],
                    hiring_region=job['hiring_region'],
                    hiring_contact=job['hiring_contact'],
                    hiring_reference=job['hiring_reference'],
                    job_id=job['job_id'],
                    description=job['description'])"""
            db.session.add(job)
            db.session.commit()

        return 'Got some jobs!'

if __name__ == '__main__':
    app.run(debug=True)

# employee_data = {'firstname':'John','lastname':'Smith'}
# employee = Employee(**employee_data)
# db.session.add(employee)
# db.session.commit()