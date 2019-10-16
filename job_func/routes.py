from flask import render_template, url_for, flash, redirect, request
from job_func.models import Job
from job_func import app, db
from job_func import job_search


@app.route('/')
def search():
    return render_template('search_jobs.html')


@app.route('/get_jobs', methods=['POST', 'GET'])
def get_jobs():
    jobs = []
    if request.method == 'POST':
        search = request.form
        keyword = search["Keyword"]
        location = search["Location"]
        radius = search["Radius"]
        posted = search["Posted"]
        jobs = job_search(keyword, location, radius, posted)

        db.create_all()
        for job in jobs:
            job = Job(**job)
            db.session.add(job)
            db.session.commit()

        return render_template('job_results.html', job_results=jobs)



