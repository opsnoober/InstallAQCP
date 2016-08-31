import sys
import os
import shutil
import subprocess
sys.path.append('../')
from utils.log import Logger

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_kav.lck')
logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=
1,logger='install_kav').getlog()

def recover_libs():
    deb_list = []
    for deb_pkg in os.listdir(os.path.join(os.path.dirname(basedir),'libs','debs','archives')):
        if os.path.splitext(os.path.join(os.path.dirname(basedir),'libs','debs','archives',deb_pkg))[1] == ".deb":
            deb_list.append(deb_pkg)
    for deb in deb_list:
        child = subprocess.Popen(['dpkg','-i',os.path.join(os.path.dirname(basedir),'libs','debs','archives',deb)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        (out,err) = child.communicate()
        logger.info(out)
        if err:
            logger.error(err)

def install_kav():
    pass

def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        logger.info('++++++++++++++ start install_kav ++++++++++++++++++')
        recover_libs()
        install_kav()
        os.mknod(lockfile)
        logger.info('++++++++++++++ end install_kav ++++++++++++++++++')


if __name__ == "__main__":
    run()
