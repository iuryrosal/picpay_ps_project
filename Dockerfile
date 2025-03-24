FROM python:3.11-buster

RUN pip install poetry==1.4.2

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY api controller db infra models repositories schemas service ./
RUN touch README.md

RUN poetry install --without dev

EXPOSE 8080

ENTRYPOINT ["poetry", "run", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]