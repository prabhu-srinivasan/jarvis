from flask import Flask
from jarvis.blueprint import jarvis


app = Flask(__name__, static_url_path='/static')
app.register_blueprint(jarvis)
