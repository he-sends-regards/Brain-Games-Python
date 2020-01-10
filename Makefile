run:
	poetry run brain-games

install:
	poetry install

publish:
	poetry build
	poetry publish

lint:
	poetry run flake8 brain_games
