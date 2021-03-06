FROM python:3.6.2rc2

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip pipenv && \
    pipenv install --system --deploy --ignore-pipfile
