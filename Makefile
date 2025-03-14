.ONESHELL:
VENV           = .venv

init: clean
	python -m venv $(VENV) 
	source $(VENV)/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

clean: 
	rm -rf $(VENV) dist
	find -iname "*.pyc" -delete

build:
	uv build

.PHONY: build
