FROM continuumio/miniconda3:4.9.2-alpine

COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip3 install kafka-python PyMySQL

CMD python load_db.py