#!/bin/bash
nginx -c /home/xeem-api/proxy-conf/nginx.conf
python /home/xeem-api/run.py