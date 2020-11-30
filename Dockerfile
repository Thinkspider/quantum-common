FROM python:3.9.0-buster

ENV TZ=UTC
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && \
    apt upgrade -y && \
    apt autoremove -y --purge && \
    apt clean -y && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /app

ADD Pipfile /app

ADD Pipfile.lock /app

WORKDIR /app

RUN pip install --no-cache-dir pipenv && pipenv install --system --deploy --ignore-pipfile --clear && pip uninstall --yes pipenv && rm -rf ~/.cache/

RUN touch .env

ADD . /app


CMD sh entrypoint.sh



