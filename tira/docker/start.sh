#!/bin/bash
/etc/init.d/nginx restart
/usr/local/bin/uwsgi --ini /tira/tira/docker/tira_uwsgi.ini --daemonize /var/log/tira_uwsgi.log


