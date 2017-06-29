from flask import Flask

from jarvis.blueprint import jarvis


context = ('ssl/server.crt', 'ssl/server.key')
app = Flask(__name__, static_url_path='/static')
app.register_blueprint(jarvis)
app.run(host='0.0.0.0', port=8000, debug=True, threaded=True, ssl_context=context)
