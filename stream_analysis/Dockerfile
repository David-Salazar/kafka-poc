FROM huggingface/transformers-pytorch-gpu:4.2.2

COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN pip3 install kafka-python && python hfmodels.py

CMD python analyze_streams.py