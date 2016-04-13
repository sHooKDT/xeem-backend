FROM python:3-onbuild
RUN apt-get update && apt-get install -y git python-pip
RUN git clone https://github.com/sHooKDT/xeem-backend.git
RUN pip install eve
CMD ["python", "xeem-backend/run.py"]
