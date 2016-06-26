FROM django:latest

MAINTAINER Samuel Kurath <skurath@hsr.ch>

ENV STRONGSWAN_VERSION 5.4.0

ADD mysite_nginx.conf /etc/strongswan.conf

&& apt-get update \
&& apt-get install -y nginx python-pip python-dev \
&& export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp34-cp34m-linux_x86_64.whl \
&& pip3 install --upgrade $TF_BINARY_URL \
&& pip install --upgrade pip \
&& pip install uwsgi \
&& mkdir -p /etc/uwsgi/sites \
&& cd /etc/uwsgi/sites \
&& cd / \
&& git clone https://github.com/Murthy10/tira.git \
&& ln -s /tira/tira/docker/mysite_nginx.conf /etc/nginx/sites-enabled/ \
&& cd /tira/ \
&& python manage.py collectstatic \
&& service nginx restart \
&& service uwsgi start \
