FROM python:3.11-slim

RUN mkdir /src
WORKDIR /src

COPY . /src
RUN pip install -U pip && pip3 install -r requirements.txt

CMD gunicorn --bind=0.0.0.0:9696 predict:app
