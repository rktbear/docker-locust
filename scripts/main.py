from locust import HttpLocust, TaskSet, task
import os

class UserBehaviour(TaskSet):
    @task
    def task(self):
        print "A fake task! Write a test!"

class User(HttpLocust):
    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 15000

    # This line is here to allow the host to be set in an environment variable
    # when running inside a Docker container!
    host = os.environ["LOCUST_HOST"]
