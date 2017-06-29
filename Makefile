.PHONY: clean install server run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '*DS_Store*' -delete

install:
	pip install -r requirements.txt

server:
	PYTHONPATH=visual_recognition	FLASK_APP=app.py python -m flask run

run: clean server

all: clean install server
