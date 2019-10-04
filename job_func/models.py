from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
#from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer(), primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)
    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_keyword = db.Column(db.String(100), nullable=False)
    search_location = db.Column(db.String(100), nullable=False)
    search_radius = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    valid_through = db.Column(db.DateTime, nullable=False)
    hiring_organisation = db.Column(db.String(100), nullable=False)
    hiring_city = db.Column(db.String(100), nullable=False)
    hiring_region = db.Column(db.String(100), nullable=False)
    hiring_contact = db.Column(db.String(100), nullable=False)
    hiring_reference = db.Column(db.String(100), nullable=False)
    job_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Job('{self.title}', '{self.date_posted}', '{self.valid_through}')"


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"
