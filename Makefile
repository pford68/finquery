VENV := ./.venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

venv: $(VENV)/bin/activate

test: venv
	$(VENV)/bin/python3 -m pytest -v tests

lint: venv
	$(VENV)/bin/python3 -m flake8 -v app