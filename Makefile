run:
	poetry run brain-games

configure:
	poetry install

install:
	poetry install

publish:
	poetry build
	poetry publish

lint:
	poetry run flake8 brain_games
