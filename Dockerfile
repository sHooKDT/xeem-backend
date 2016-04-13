FROM ubuntu:trusty
RUN apt-get update && apt-get install -y python python-pip git
RUN pip install eve

WORKDIR /home

RUN git clone -b master https://github.com/sHooKDT/xeem-backend.git xeem-api
CMD ["nginx", "-c /home/xeem-api/proxy-conf/nginx.conf"]
RUN chmod +x xeem-api/run.py
CMD ["nohup", "xeem-api/run.py &"]

EXPOSE 500
EXPOSE 81