# docker-locust

A Docker container that can run the load testing framework [locust.io](http://locust.io).

## Usage

### Build the Docker Image

`docker build -t locust /path/to/dockerfile`

### Run Locust - Single Node

The docker container acts as a locust executable so all arguments after the container is run are parsed to locust.

__IMPORTANT__: No Locust test scripts are built into the image so you must mount a path on the host where the scripts are found (e.g. `/path/to/locustfiles/`).

`docker run -p 8089:8089 -v /path/to/locustfiles:/opt/locust -f /opt/locust/locustfile.py`
