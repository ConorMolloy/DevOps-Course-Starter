FROM python:3.7.9-slim-buster as base

ENV PATH /usr/local/bin:$PATH
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app
RUN pip install poetry
EXPOSE 5000
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root
COPY . /app

FROM base as production
ENTRYPOINT poetry run gunicorn -w 4 -b 0.0.0.0:5000 run:app

FROM base as development
ENTRYPOINT poetry run flask run --host=0.0.0.0

FROM base as test
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update \
  && apt-get install --no-install-recommends --no-install-suggests --assume-yes \
  curl \
  bzip2 \
  libgtk-3-0 \
  libdbus-glib-1-2 \
  xvfb \
  && FIREFOX_DOWNLOAD_URL='https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64' \
  && curl -sL "$FIREFOX_DOWNLOAD_URL" | tar -xj -C /opt \
  && ln -s /opt/firefox/firefox /usr/local/bin/ \
  && BASE_URL='https://github.com/mozilla/geckodriver/releases/download' \
  && VERSION=$(curl -sL 'https://api.github.com/repos/mozilla/geckodriver/releases/latest' | grep tag_name | cut -d '"' -f 4) \
  && curl -sL "${BASE_URL}/${VERSION}/geckodriver-${VERSION}-linux64.tar.gz" | tar -xz -C /usr/local/bin \
  && apt-get purge -y \
  curl \
  bzip2

ENTRYPOINT ["poetry", "run", "pytest"]