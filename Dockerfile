FROM debian:latest

RUN apt-get update
RUN apt-get install -y python python-dev
RUN apt-get install -y python-pip
RUN pip install locustio

EXPOSE 8089

ENTRYPOINT ["locust"]
