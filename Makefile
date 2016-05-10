init:
	pip install -r requirements.txt

requirements:
	pip freeze > requirements.txt

test:
	nosetests tests
