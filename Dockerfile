FROM python:3.7.9-slim-buster

ENV PATH /usr/local/bin:$PATH
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
RUN pip install poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root
COPY . /app

EXPOSE 5000

ENTRYPOINT poetry run gunicorn -w 4 -b 0.0.0.0:5000 run:app