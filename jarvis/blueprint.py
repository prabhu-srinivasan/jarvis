import json
import wikipedia
import requests

from flask import request, Blueprint, render_template
from watson_services import tone_analyzer, translate, query_collection


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
    result = translate(text, format)
    return result if result else ''


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
    emotion, joke = '', ''
    input_text = request.values.get('text')
    tones = tone_analyzer(input_text)
    tones = tones.get('document_tone', {}).get('tone_categories', [])
    for tone in tones:
        if tone.get('category_id') == 'emotion_tone':
            tones = tone.get('tones')
            break
    tones = sorted(tones, key=lambda x: x['score'])
    final_tone = tones.pop()
    emotion = final_tone.get('tone_name')
    joke = requests.get('http://api.icndb.com/jokes/random')
    joke = json.loads(joke.content)
    joke = joke['value']['joke']
    return json.dumps({'emotion': emotion, 'joke': joke})


@jarvis.route('/tasks/insights')
def tasks_insights():
    return render_template('analyze.html')


@jarvis.route('/tasks/review')
def tasks_review():
    review_results = {}
    keyword_results = []
    review_query = {'aggregation': 'term(enriched_text.docSentiment.type,count:3)'}
    keywords_query = {'aggregation': 'term(enriched_text.keywords.text,count:5)'}
    reviews = query_collection(review_query)
    keywords = query_collection(keywords_query)
    reviews = reviews['aggregations'][0]['results']
    keywords = keywords['aggregations'][0]['results']
    for review in reviews:
        key = review.get('key')
        value = review.get('matching_results')
        review_results.update({key: value})
    for keyword in keywords:
        keyword_results.append(keyword.get('key'))
    return render_template('review.html', reviews=review_results, keywords=keyword_results)
