FROM ubuntu:16.04
MAINTAINER Ivan Semenyshyn
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update
RUN apt-get install -y python-pip python-dev python-lxml libxml2-dev libxslt1-dev libxslt-dev libpq-dev && apt-get clean
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /todolist

EXPOSE 80