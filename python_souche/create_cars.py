# -*- coding: UTF-8 -*-
import requests


class Requests_methon(object):
    def __init__(self,
                 url, headers):

        self.url = url
        self.headers = headers

    def request_get(self):
        #requests.get(url=self.url, headers=self.headers)
        print(self.url, self.headers)


if __name__ == "__main__":
    request1s = Requests_methon('22', '23123')
    request1s.request_get()

