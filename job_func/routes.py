from flask import render_template, url_for, flash, redirect, request
from job_func.models import Job, ApplicationStage
from job_func import app, db
from job_func import job_search
from job_func.forms import JobSearchForm, StageForm
from datetime import datetime
today = datetime.now().strftime('%Y-%m-%d') + ' 00:00:00'


@app.route("/")
@app.route('/Search')
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
            job_id_exist = Job.query.filter_by(job_id=job.job_id).first()
            if job_id_exist:
                pass
            else:
                db.session.add(job)
        db.session.commit()

        jobs = Job.query.order_by(Job.date_posted.desc())

        return render_template('job_results.html', title='Job Results',
                               job_results=jobs)


@app.route('/jobs/<query_filter>')
def jobs(query_filter):
    if query_filter == "all":
        jobs = Job.query.order_by(Job.date_posted.desc())
    elif query_filter == "today":
        jobs = Job.query.filter(Job.date_added >= today).all()
    else:
        jobs = Job.query.filter(Job.date_applied != 'Null')
    return render_template('job_results.html',
                           title='Jobs', job_results=jobs, status='applied')


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
