FROM debian:latest

RUN apt-get update
RUN apt-get install -y python python-dev
RUN apt-get install -y python-pip
RUN pip install locustio

RUN mkdir -p /locust/scripts
ADD ./scripts/main.py /locust/scripts/main.py
ADD ./scripts/docker.py /locust/scripts/docker.py

EXPOSE 8089

ENV REQUEST_LOG "/locust/requests.log"

ENTRYPOINT ["locust", "-f", "/locust/scripts/main.py"]
