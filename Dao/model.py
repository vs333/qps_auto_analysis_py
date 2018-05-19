# -*- coding: utf-8 -*-


from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import *
Base = declarative_base()


class nginx_server_info(Base):
    __tablename__ = "gray_nginx_server_info"
    id = Column(Integer, primary_key=True, autoincrement=True)
    NginxName = Column(VARCHAR(50))
    PrivateIp = Column(VARCHAR(50))
    Env = Column(VARCHAR(50))
