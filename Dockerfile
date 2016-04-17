FROM ubuntu:trusty
RUN apt-get update && apt-get install -y python python-pip git nginx
RUN pip install eve

WORKDIR /home

RUN git clone -b master https://github.com/sHooKDT/xeem-backend.git xeem-api
RUN chmod +x /home/xeem-api/run.sh
# CMD nginx -c /home/xeem-api/proxy-conf/nginx.conf && python /home/xeem-api/run.py
CMD bash /home/xeem-api/run.sh

EXPOSE 500
EXPOSE 81