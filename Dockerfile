FROM ubuntu:trusty
RUN apt-get update && apt-get install -y python python-pip git
RUN pip install eve

WORKDIR /home

EXPOSE 500

RUN git clone -b master https://github.com/sHooKDT/xeem-backend.git xeem-api
CMD ["nginx", "-c /home/xeem-api/proxy-conf/nginx.conf"]
CMD ["python", "xeem-api/run.py"]
