FROM docker.arvancloud.ir/python:3.12-alpine

RUN pip install --upgrade pip && \
    apt install libpq5 && \
    pip install -r prod.txt \
