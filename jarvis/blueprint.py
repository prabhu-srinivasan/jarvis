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
    # speech to text
    response = wikipedia.page(text)
    return response.content


@jarvis.route('/tasks/monitor')
def tasks_monitor():
    return render_template('monitor.html')


@jarvis.route('/apis/monitor', methods=['POST'])
def apis_monitor():
    emotion, joke = 'sad', ''
    # call the tone analyzer and return emotion
    joke = requests.get('http://api.icndb.com/jokes/random')
    joke = json.loads(joke.content)
    joke = joke['value']['joke']
    return json.dumps({'emotion': emotion, 'joke': joke})

@jarvis.route('/tasks/insights')
def tasks_insights():
    return 'Insights !!'
