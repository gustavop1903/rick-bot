FROM python:3.11
WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetryc config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 7002
CMD ["python", "run.py"]
