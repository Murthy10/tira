FROM django:latest

MAINTAINER Samuel Kurath <skurath@hsr.ch>

RUN apt-get update \
&& apt-get install -y nginx python-pip python-dev \
&& export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp34-cp34m-linux_x86_64.whl git vim \
&& pip install --upgrade pip \
&& pip3 install --upgrade $TF_BINARY_URL \
&& pip install uwsgi \
&& cd / \
&& git clone https://github.com/Murthy10/tira.git \
&& ln -s /tira/tira/docker/mysite_nginx.conf /etc/nginx/sites-enabled/ \
&& cd /tira/ \
&& python manage.py collectstatic \

