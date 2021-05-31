FROM python:3.9.5 as base

RUN pip install poetry
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

FROM base as production
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev
COPY . /code
ENV PORT 5000
RUN chmod +x scripts/prod-entrypoint.sh
ENTRYPOINT ["scripts/prod-entrypoint.sh"]

FROM base as development
RUN poetry config virtualenvs.create false && \
    poetry install --no-root
COPY . /code
EXPOSE 5000
ENTRYPOINT ["poetry", "run", "flask", "run", "-h", "0.0.0.0"]

FROM base as test
RUN poetry config virtualenvs.create false && \
    poetry install --no-root
COPY . /code
EXPOSE 5000
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