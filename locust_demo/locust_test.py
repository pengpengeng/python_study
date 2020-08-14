# -*- coding: UTF-8 -*=
import os
import sys

# from locust import HttpLocust,TaskSet,task,between

# class demo(TaskSet):
#     @task
#     def get_demo():
#         self.client.get("http://www.baidu.com")

# class WebsiteUser(HttpLocust):
#     task_set=demo
#     host="http://www.baidu.com"
#     wait_time=between(2,5)

# if __name__ == "__main__":
#     cmd = 'locust -f locust_test.py'
#     os.system(cmd)
data=sys.argv
print(data)
for i in data:
    print(i)