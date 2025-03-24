all: setup database tests clean run

setup:
	poetry install

database:
	poetry run python -m db.init_db

clean:
	rm -rf __pycache__

run:
	poetry run uvicorn api.app:app --host 0.0.0.0 --port 8080
