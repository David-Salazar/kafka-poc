FROM continuumio/miniconda3:4.9.2-alpine

COPY . /usr/local/python/

WORKDIR /usr/local/python/

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "docker-stats", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "docker-stats", "voila", "data_analysis.ipynb"]

EXPOSE 8866/tcp
