FROM docker.arvancloud.ir/python:3.12-alpine

RUN pip install --upgrade pip && \
    apk install libpq5 && \
    pip install -r requirements.txt
