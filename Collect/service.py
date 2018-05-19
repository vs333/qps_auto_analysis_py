# -*- coding: utf-8 -*-

import json


class Base(object):
    def __init__(self):
        pass

    @classmethod
    def regular_response(cls, string):
        print string
        urls = json.loads(string)
        for item in urls:
            url = item.get("url").split(":")[0]
            item["datetime"] = long(item.get("url").split(":")[-1])
            try:
                item["average"] = item.get("time") / item.get("qps")
            except TypeError:
                continue
            item["url"] = url
        return urls
