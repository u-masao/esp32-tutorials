.PHONY: all test clean

runserver:
	poetry run python -m src.server.main

test:
	cd test ; poetry run py.test server.py

