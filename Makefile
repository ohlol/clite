ACTIVATE = .venv/bin/activate
CLITE = .venv/bin/clite

$(ACTIVATE):
	python3 -m venv .venv

$(CLITE): $(ACTIVATE) pyproject.toml
	. $(ACTIVATE); \
		python3 -m pip install -e .[dev]

clean:
	rm -rf .venv

install-dev: $(CLITE)
	@true

mypy: $(CLITE)
	. $(ACTIVATE); \
		mypy src

test: $(CLITE)
	. $(ACTIVATE); \
		env PYTHONPATH=src python3 -m pytest

venv: $(ACTIVATE)
	@true

.PHONY: clean install-dev mypy test venv
