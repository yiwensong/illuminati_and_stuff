.PHONY: venv
venv:
	tox -e venv

.PHONY: install-hooks
install-hooks:
	tox -e install-hooks

.PHONY: test
test:
	tox
