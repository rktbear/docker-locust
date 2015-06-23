from locust import TaskSet, task
import docker

docker.init()

class UserBehaviour(TaskSet):
    @task
    def task(self):
        response = docker.post(client, "/test/url/10", "some_data")
        print "Response Code: " + response.status_code

class User(docker.DockerHttpLocust):
    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 15000
