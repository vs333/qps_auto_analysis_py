# -*- coding: utf-8 -*-
import Http.Service
import Collect.service
import datetime


class Base(object):
    def __init__(self, nginx_ip):
        self.date = long(datetime.datetime.now().strftime('%Y%m%d%H%M'))
        self.htp = Http.Service.Base(nginx_ip)
        self.nginx_ip = nginx_ip

    def converter_qps(self):
        result = self.htp.get()
        data = Collect.service.Base.regular_response(result)
        return data

    def qps_limit(self):
        data = self.converter_qps()
        start_message = "开始分析RT值，时间:{0}".format(self.date)
        print start_message
        for item in data:
            if item.get("datetime") != self.date - 1 or item.get("average") < 4000:
                continue
            limit_qps = 20000
            if item.get("average") >= 10000:
                limit_qps = 1000
            elif item.get("average") >= 8000:
                limit_qps = 2500
            elif item.get("average") >= 6000:
                limit_qps = 4000
            elif item.get("average") >= 4000:
                limit_qps = 6000
            message = "服务器ip：{4};限流url：{0};时间：{6};平均返回时间毫秒：{1};总耗时毫秒：{2};请求数：{3};设置阈值：{5}".format(
                item.get("url"),
                item.get("average"),
                item.get("time"),
                item.get("qps"),
                self.nginx_ip,
                limit_qps,
                item.get(
                    "datetime"))
            print message
            self.htp.post(item.get("url"), limit_qps, 59)
