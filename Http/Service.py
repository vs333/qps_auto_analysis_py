# -*- coding: utf-8 -*-

import requests


class Base(object):

    def __init__(self, ip):
        self.ip = ip
        self.headers = {"Host": "limitqps.xxxxxxxx.net"}

    def get(self):
        uri = "action"
        url = "http://{0}/{1}?action=show".format(self.ip, uri)
        req = requests.get(url, headers=self.headers)
        return req.text

    def post(self, url_key, limit_value, expiretime):
        uri = "action"
        url = "http://{0}/{1}".format(self.ip, uri)
        data = {
            "urlkey": url_key,
            "limitvalue": limit_value,
            "expiretime": expiretime
        }
        req = requests.post(url, data=data, headers=self.headers)
        print req.text

