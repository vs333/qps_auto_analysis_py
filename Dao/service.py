# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import Dao.model


class db_ops(object):
    def __init__(self, Base=declarative_base()):
        self.sessiondb = self.conndb(Base)

    def conndb(self, Base):
        engine_db = create_engine('mysql://root:password@x.x.x.x:43306/devops')
        session_db = sessionmaker(bind=engine_db)
        sessiondb = session_db()
        Base.metadata.create_all(engine_db)
        return sessiondb

    def close(self):
        self.sessiondb.close()
    def select_nginx_ip(self):
        tmplist = list()
        result = self.sessiondb.query(Dao.model.nginx_server_info).filter(
            Dao.model.nginx_server_info.Env == "net").all()
        for item in result:
            tmplist.append(item.PrivateIp)
        return tmplist
