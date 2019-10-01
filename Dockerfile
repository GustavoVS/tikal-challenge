FROM python:3.6

LABEL Name=tikal-challenge Version=0.0.1
# env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# pipenv
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --ignore-pipfile --system

COPY . /code/
