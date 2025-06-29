FROM docker.arvancloud.ir/python:3.12-alpine

COPY requirements.txt .

RUN pip install --upgrade pip && \
#    apk add libpq5 && \
    pip install -r ./requirements.txt
