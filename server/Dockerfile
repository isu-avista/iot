# get base image
FROM balenalib/raspberry-pi-debian:latest

# create working directory
WORKDIR ./

# install dependencies
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

# copy requirements
COPY ./requirements.txt ./requirements.txt

# install python dependencies
RUN pip3 install -r requirements.txt

# copy application files
COPY ./ ./