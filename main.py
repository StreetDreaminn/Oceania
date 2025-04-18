from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/home')
@login_required
def home():
    return render_template('home.html', name=current_user.name)

@main.route('/quiz')
@login_required
def quiz():
    return render_template('quiz.html')

@main.route('/dob')
@login_required
def dob():
    return render_template('dob.html')

@main.route('/info')
@login_required
def info():
    return render_template('info.html')