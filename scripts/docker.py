from locust import HttpLocust
import os
import time

class DockerHttpLocust(HttpLocust):
    host = os.environ["LOCUST_HOST"]

log_file = None

def get_time_ms():
    return int(time.time()*1000)

def init():
    global log_file
    file_name = os.environ["REQUEST_LOG"]
    log_file = open(file_name, "w")

def write_log(s):
    global log_file
    log_file.write("%d %s\n" % (get_time_ms(), s))

def post(client, url, data=""):
    start_ms = get_time_ms()
    response = client.post(url, data)
    end_ms = get_time_ms()
    write_log("%d POST %s %s" % ((end_ms-start_ms), url, response.status_code))
    return response

def put(client, url, data=""):
    start_ms = get_time_ms()
    response = client.put(url, data)
    end_ms = get_time_ms()
    write_log("%d PUT %s %s" % ((end_ms-start_ms), url, response.status_code))
    return response

def get(client, url, data=""):
    start_ms = get_time_ms()
    response = client.get(url, data)
    end_ms = get_time_ms()
    write_log("%d GET %s %s" % ((end_ms-start_ms), url, response.status_code))
    return response
