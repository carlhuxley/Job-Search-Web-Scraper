from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length


class JobSearchForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired(),
                                                 Length(max=30)])
    location = StringField('Location', validators=[Length(max=20)])
    radius = IntegerField('Radius')
    posted = IntegerField('Posted Within')
    submit = SubmitField('Get Jobs')


class StageForm(FlaskForm):
    job_id = IntegerField('Job ID')
    status = StringField('status', validators=[DataRequired(), Length(max=20)])
    note = TextAreaField('note')
    submit = SubmitField('Create Stage')
