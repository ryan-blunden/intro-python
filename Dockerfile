FROM python:3.6.3-slim

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y make nano wget jq && \
    rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile

RUN pip3 install pip setuptools --upgrade && \
    pip3 install pipenv && \
    pipenv install --deploy --system
