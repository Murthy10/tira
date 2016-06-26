#!/bin/bash
/etc/init.d/nginx restart
/usr/local/bin/uwsgi --ini /tira/tira/docker/tira_uwsgi.ini


