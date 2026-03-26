.PHONY: run shell clean 


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

check-requirements:
	@grep -hE '^(import|from) [a-zA-Z0-9_]+' src/*.py | sed -E 's/^(import|from) ([a-zA-Z0-9_]+).*/\2/' | sort -u > .imports_temp
	@errors=0; \
	
	@while read import; do \
		if ! $(PYTHON) -c "import $$import" 2>/dev/null; then \
			echo "Module '$$import' not founded in virtual environment"; \
			errors=$$((errors + 1)); \
		fi; \
	done < .imports_temp; \
	\
	if [ $$errors -gt 0 ]; then \
		echo "Not founded modules: $$errors. Please install it"; \
		exit 1; \
	else \
		echo "All modules found"; \
	fi
