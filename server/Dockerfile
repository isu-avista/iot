FROM ubuntu:20.04

ARG ssh_prv_key
ARG ssh_pub_key

WORKDIR ./

RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get install -y python-dev
RUN apt-get install -y gunicorn
RUN apt-get install -y git

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
