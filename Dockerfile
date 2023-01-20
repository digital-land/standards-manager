# Dockerfile
FROM python:3.11.0-slim  as base

RUN set -ex; \
    apt-get update; \
    apt-get upgrade --assume-yes; \
    apt-get install --assume-yes  \
    build-essential \
    curl \
    git

WORKDIR /app
COPY . /app

RUN set -ex; \
    curl -s https://deb.nodesource.com/setup_16.x | bash;\
    apt-get install --assume-yes nodejs; \
    npm install;

RUN python -m pip install --upgrade pip
RUN python -m pip install pip-tools
RUN python -m piptools compile requirements/requirements.in
RUN python -m piptools compile requirements/dev-requirements.in
RUN python -m piptools sync requirements/requirements.txt requirements/dev-requirements.txt


FROM base AS development
CMD flask run -h 0.0.0.0
