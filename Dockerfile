FROM ubuntu:trusty
RUN apt-get update && apt-get install -y python python-pip git nginx
RUN pip install eve

WORKDIR /home

RUN git clone -b master https://github.com/sHooKDT/xeem-backend.git xeem-api
RUN nginx -c /home/xeem-api/proxy-conf/nginx.conf
RUN python /home/xeem-api/run.py &

EXPOSE 500
EXPOSE 81