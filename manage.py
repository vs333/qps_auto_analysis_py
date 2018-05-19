# -*- coding: utf-8 -*-

import time
import Dao.service
import Analysis.service
import traceback
import Scueduler.service
import logging

def start_qps_limit(db):
    nginx_list = db.select_nginx_ip()
    for nginx_ip in nginx_list:
        ans = Analysis.service.Base(nginx_ip)
        ans.qps_limit()
    db.close()


if __name__ == "__main__":
    db = Dao.service.db_ops()
    logging.basicConfig()
    apsc = Scueduler.service.Myscheduler()
    try:
        apsc.scheduler.add_job(start_qps_limit, "cron", args=(db,), minute='*/1')
        print "APscheduler add job ..."
        apsc.scheduler.start()
        print "APscheduler start ..."
        while True:
            time.sleep(10)
    except Exception, e:
        print traceback.print_exc()
        exit(1)
