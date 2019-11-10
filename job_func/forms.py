from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField
from job_func.models import Choice


class JobSearchForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired(),
                                                 Length(max=30)])
    location = StringField('Location', validators=[Length(max=20)])
    radius = IntegerField('Radius')
    posted = IntegerField('Posted Within')
    submit = SubmitField('Get Jobs')


def choice_query():
    return Choice.query


def get_pk(obj):
    return str(obj)


class StageForm(FlaskForm):
    job_id = IntegerField('Job ID')
    status = QuerySelectField(query_factory=choice_query,
                              allow_blank=False, get_label='name', get_pk=get_pk)
    note = TextAreaField('note')
    submit = SubmitField('Create Stage')


class ChoiceForm(FlaskForm):
    opts = QuerySelectField(query_factory=choice_query, allow_blank=False, get_label='name', get_pk=get_pk)
