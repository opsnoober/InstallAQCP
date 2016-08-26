#-*-coding:utf-8-*-
from log import Logger
import os

basedir = os.path.split(os.path.realpath(__file__))[0] 
logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=1,logger='InstallAQCP').getlog()

def add_log(func):
    def _wrapper():
        logger.info("+++++++++++++ begin  +++++++++++++++++++++++")
        func()
        logger.info("+++++++++++++ finish  +++++++++++++++++++++++")
    return _wrapper
