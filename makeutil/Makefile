.PHONY: run clean 

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/PIP

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate


run: $(VENV)/bin/activate
	$(PYTHON) src/app.py

shell: $(VENV)/bin/activate
	
	@echo "entering venv, type exit to quit"
	@PATH=$(shell pwd)/$(VENV)/bin:$$PATH bash

clean:
	rm -rf $(VENV)