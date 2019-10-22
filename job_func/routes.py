from flask import render_template, url_for, flash, redirect, request
from job_func.models import Job, ApplicationStage
from job_func import app, db
from job_func import job_search
from job_func.forms import JobSearchForm, StageForm


@app.route('/')
def search():
    form = JobSearchForm()
    return render_template('search_jobs.html', title='Search Jobs', form=form)


@app.route('/get_jobs', methods=['POST', 'GET'])
def get_jobs():
    jobs = []
    if request.method == 'POST':
        search = request.form
        keyword = search["keyword"]
        location = search["location"]
        radius = search["radius"]
        posted = search["posted"]
        jobs = job_search(keyword, location, radius, posted)

        db.create_all()
        for job in jobs:
            job = Job(**job)
            db.session.add(job)
            db.session.commit()

        jobs = Job.query.order_by(Job.date_posted.desc())

        return render_template('job_results.html', title='Job Results',
                               job_results=jobs)


@app.route('/application_stage/new', methods=['GET', 'POST'])
def new_application_stage():
    form = StageForm()
    if form.validate_on_submit():
        stage = ApplicationStage(status=form.status.data, note=form.note.data, job_id=form.job_id.data)
        db.session.add(stage)
        db.session.commit()
        flash('Your Application Stage has been created!', 'success')
        return redirect(url_for('search'))
    return render_template('create_application_stage.html',
                           title='New Application Stage', form=form)


@app.route("/job_detail/<int:job_id>")
def job_detail(job_id):
        job = Job.query.get_or_404(job_id)
        return render_template('job_detail.html', title=job.title, job=job)
