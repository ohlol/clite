base_requirements = requirements/base.txt
dev_requirements = requirements/dev.txt

mypy: update-pip setup-dev
	mypy src

setup: update-pip
	. .venv/bin/activate; \
		python3 -m piptools sync $(base_requirements)

setup-dev: setup
	. .venv/bin/activate; \
		python3 -m piptools sync $(dev_requirements)

update: update-pip
	mkdir -p requirements
	. .venv/bin/activate; \
		python3 -m piptools compile -o $(base_requirements) pyproject.toml

update-dev: update
	. .venv/bin/activate; \
		python3 -m piptools compile -o $(dev_requirements) --extra dev pyproject.toml
	pre-commit autoupdate

update-pip:
	. .venv/bin/activate; \
		python3 -m pip install -U pip pip-tools setuptools

venv:
	python3 -m venv .venv

.PHONY: setup setup-dev update update-dev update-pip
