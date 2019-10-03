FROM python:3.6

LABEL Name=tikal-challenge Version=0.0.1

# env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code


# node and npm dependencies

RUN apt update \
    && apt install -y curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt install -y nodejs
RUN npm install


# pipenv

RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --ignore-pipfile --system

COPY . /code/
