# pull official base image
FROM python:3.10-slim-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

RUN apt-get update
RUN apt-get install -y netcat-openbsd
RUN apt-get install -y --fix-missing pkg-config default-mysql-client python3-dev default-libmysqlclient-dev build-essential
RUN apt-get update --fix-missing

COPY ./docker-entrypoint.sh .
RUN chmod +x ./docker-entrypoint.sh

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

ENTRYPOINT [ "./docker-entrypoint.sh" ]



