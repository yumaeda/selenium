FROM python:3

WORKDIR /var/lib/python3

RUN set -x && \
    apt-get update && \
    apt-get install -y vim

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
