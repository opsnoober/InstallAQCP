import sys
import os
import shutil
import subprocess
sys.path.append('../')
from utils.log import Logger

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_base.lck')
logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=
1,logger='install_base').getlog()
base_list = ['gcc','g++','make','zip','unzip','lrzsz','python-pip','python-dev']

def install_base():
    for base_pkg in base_list:
        child = subprocess.Popen(['apt-get','-y','install',base_pkg],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        (out,err) = child.communicate()
        logger.info(out)
        if err:
            logger.error(err)
    

def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        logger.info('++++++++++++++ start install_base ++++++++++++++++++')
        install_base()
        os.mknod(lockfile)
        logger.info('++++++++++++++ end install_base ++++++++++++++++++')


if __name__ == "__main__":
    run()
