FROM continuumio/miniconda3:4.9.2-alpine

COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip3 install transformers[torch] kafka-python && python hfmodels.py

CMD python analyze_streams.py