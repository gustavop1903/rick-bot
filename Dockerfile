FROM python:3.12
WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

EXPOSE 7002
CMD ["python", "run.py"]
