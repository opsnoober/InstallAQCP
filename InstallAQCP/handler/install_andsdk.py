import sys
import os
import shutil
import subprocess
sys.path.append('../')
from utils.log import Logger
from utils.config import Get_data

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_andsdk.lck')
logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=
1,logger='install_andsdk').getlog()
android_sdk = os.path.join(os.path.dirname(basedir),'libs','res','android-sdk-linux.tar.gz')
getdata = Get_data(os.path.join(os.path.dirname(basedir),'conf.ini'))
user = getdata.Show_option_data('global','user')
group = getdata.Show_option_data('global','group')


def install_andsdk():
    child = subprocess.Popen(['tar','zxvf',android_sdk,'-C','/usr/'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out,err) = child.communicate()
    logger.info(out)
    if err:
        logger.error(err)
    subprocess.check_call(['chown','-R','%s:%s'%(user,group),'/usr/android-sdk-linux'])
    

def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        logger.info('++++++++++++++ start install_andsdk ++++++++++++++++++')
        install_andsdk()
        os.mknod(lockfile)
        logger.info('++++++++++++++ end install_andsdk ++++++++++++++++++')


if __name__ == "__main__":
    run()
