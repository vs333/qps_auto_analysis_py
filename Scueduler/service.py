# -*- coding: utf-8 -*-
import apscheduler.executors.pool
import apscheduler.schedulers.background


class Myscheduler(object):
    _instance = None

    def __init__(self):
        executors = {
            'default': {'type': 'threadpool', 'max_workers': 10},
            'processpool': apscheduler.executors.pool.ProcessPoolExecutor(max_workers=1)
        }
        job_defaults = {
            'coalesce': False,
            'max_instances': 1
        }
        self.scheduler = apscheduler.schedulers.background.BackgroundScheduler()
        self.scheduler.configure(executors=executors, job_defaults=job_defaults)
        print "APscheduler init ..."

    def start(self):
        print "APscheduler start ..."
        self.scheduler.start()
