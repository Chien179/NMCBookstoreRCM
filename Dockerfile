FROM python:3.10.13-alpine3.18
RUN apk update && apk add --no-cache  tzdata git make  build-base

RUN apk upgrade -U \
    && apk add --no-cache -u ca-certificates libva-intel-driver mpc1-dev libffi-dev build-base supervisor python3-dev build-base linux-headers pcre-dev curl busybox-extras \
    && rm -rf /tmp/* /var/cache/* 

RUN pip install wheel

COPY requirements.txt /
RUN pip --no-cache-dir install --upgrade pip setuptools
RUN pip --no-cache-dir install -r requirements.txt
RUN mkdir -p /webapps

COPY . /webapps
WORKDIR /webapps

EXPOSE 50051

