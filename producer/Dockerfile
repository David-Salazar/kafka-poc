FROM continuumio/miniconda3

COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip3 install tweepy kafka-python

CMD python producer.py


