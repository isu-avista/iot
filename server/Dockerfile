FROM balenalib/raspberry-pi-debian:latest

ARG ssh_prv_key
ARG ssh_pub_key

WORKDIR ./

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python-dev
RUN apt-get install -y gunicorn3
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-rpi.gpio
RUN apt-get install -y python3-smbus
RUN apt-get install -y git
RUN apt-get install -y ssh
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y libpq-dev
RUN apt-get install -y gpiod libgpiod-dev

RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts


RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub


COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ ./

RUN rm -rf /root/.ssh/
