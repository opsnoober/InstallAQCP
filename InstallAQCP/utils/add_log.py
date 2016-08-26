#-*-coding:utf-8-*-
from log import Logger
import os

basedir = os.path.split(os.path.realpath(__file__))[0] 

def add_log(loggername):
    def _wrapper(func):
        logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=1,logger=str(loggername)).getlog()
        def __wrapper():
            logger.info("+++++++++++++ begin %s +++++++++++++++++++++++"%loggername)
            func()
            logger.info("+++++++++++++ finish %s +++++++++++++++++++++++"%loggername)
        return __wrapper
    return _wrapper
