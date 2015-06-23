# docker-locust

Running HTTP load tests using [locust.io](http://locust.io) within a Docker container.

The load testing script is built into the container and provides the ability to 
store HTTP request statistics to disk.

## Usage

### Writing Locust Script

An example script can be found in `scripts/main.py`.

* Import docker with `import docker`.
* Always call `docker.init()` at the top of the script.
* The locust class must sub-class `DockerHttpLocust`.
* HTTP requests must be done with: `docker.post()`, `docker.get()`, and `docker.put()`.

### Building 

1). `git pull https://github.com/rktbear/docker-locust.git`
2). Create a load test script in `./docker-locust/scripts/main.py`
3). `docker build -t locust ./docker-locust/`

### Running

`docker run -d -p 8089:8089 --name=locust -e LOCUST_HOST=$END_POINT locust --no-web -c $USERS -r $HATCH_RATE`

### View all Requests

Print out all HTTP requests. This data is only available while the container is running!

`docker exec locust cat /locust/requests.log`

The format of each request:

`<epoch_ms> <request_time_ms> <method> <url> <status_code>`

E.g.

`1435020266242 92 POST /claim/api/v1/products/test/users/0/tokens 201`
