# docker-locust

A Docker image that can run the load testing framework [locust.io](http://locust.io).

## Usage

### Building the Image

* Clone the docker-locust repo using `git pull https://github.com/rktbear/docker-locust.git`
* Store your load testing scripts in the file `./docker-locust/scripts/main.py`
* Build the Docker image using `docker build -t locust ./docker-locust/`

This will create a Docker image that can run Locust using a particular load testing script (i.e. the load testing script is bound to the image and container).

__NOTE__: The image needs to be rebuilt every time the load testing script changes!

### Run Locust - Single Node

The endpoint of the service being load tested should be set in the environment variable `LOCUST_HOST` when starting the container.

`docker run -p 8089:8089 --name=locust -e LOCUST_HOST=http://thehost.com locust`

The locust frontend will be accessible from the host at [http://127.0.0.1:8089](http://127.0.0.1:8089).

### Run Locust - Master or Slave

[TBD]
