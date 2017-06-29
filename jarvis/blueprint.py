from flask import Blueprint, render_template


jarvis = Blueprint(
    'jarvis',
    __name__,
    static_folder='static',
    template_folder='templates',
    static_url_path='/static/jarvis'
)


@jarvis.route('/')
def home():
    return render_template('home.html')


@jarvis.route('/tasks/translate')
def translate():
    return 'Translate !!'


@jarvis.route('/tasks/search')
def search():
    return 'Search !!'


@jarvis.route('/tasks/monitor')
def monitor():
    return 'Monitor !!'


@jarvis.route('/tasks/insights')
def insights():
    return 'Insights !!'
