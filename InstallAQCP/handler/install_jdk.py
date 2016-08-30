import sys
import os
import shutil
import subprocess
sys.path.append('../')
from utils.log import Logger

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_jdk.lck')
logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=
1,logger='install_jdk').getlog()
jdk = os.path.join(os.path.dirname(basedir),'libs','res','jdk-7u25-linux-x64.tar.gz')

def install_jdk():
    child = subprocess.Popen(['tar','zxvf',jdk,'-C','/usr/local/'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out,err) = child.communicate()
    logger.info(out)
    if err:
        logger.error(err)
    subprocess.check_call(['ln','-svf','/usr/local/jdk1.7.0_25','/usr/local/jdk'])
    subprocess.check_call(['ln','-svf','/usr/local/jdk1.7.0_25/bin/java','/usr/bin/java'])
    

def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        logger.info('++++++++++++++ start install_jdk ++++++++++++++++++')
        install_jdk()
        os.mknod(lockfile)
        logger.info('++++++++++++++ end install_jdk ++++++++++++++++++')


if __name__ == "__main__":
    run()
