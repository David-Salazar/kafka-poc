FROM continuumio/miniconda3

COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip3 install transformers[tf-cpu] kafka-python

CMD python analyze_streams.py