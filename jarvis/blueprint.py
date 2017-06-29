import json
import wikipedia
import requests

from flask import request, Blueprint, render_template


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
def tasks_translate():
    return render_template('translator.html')


@jarvis.route('/apis/translate', methods=['POST'])
def apis_translate():
    text = request.values.get('text')
    format = request.values.get('format')
    # call the translator
    return ''


@jarvis.route('/tasks/search')
def tasks_search():
    return render_template('search.html')


@jarvis.route('/apis/search', methods=['POST'])
def apis_search():
    text = request.values.get('text')
    response = wikipedia.page(text)
    return response.content


@jarvis.route('/tasks/monitor')
def tasks_monitor():
    return render_template('monitor.html')


@jarvis.route('/apis/monitor', methods=['POST'])
def apis_monitor():
    # call the tone analyzer and return emotion
    if emotion == 'sad':
        joke = requests.get('http://api.icndb.com/jokes/random')
        joke = json.loads(joke.content)
        return joke['value']['joke']


@jarvis.route('/tasks/insights')
def tasks_insights():
    return 'Insights !!'
