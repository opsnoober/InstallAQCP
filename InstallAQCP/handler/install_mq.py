import sys
import os
import shutil
import subprocess
sys.path.append('../')
from utils.log import Logger
from utils.config import Get_data

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_mq.lck')
logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=
1,logger='install_mq').getlog()
getdata = Get_data(os.path.join(os.path.dirname(basedir),'conf.ini'))
mq_host = getdata.Show_option_data('mq','mq_host')
mq_user = getdata.Show_option_data('mq','mq_user')
mq_pass = getdata.Show_option_data('mq','mq_pass')


def install_mq():
    child = subprocess.Popen(['apt-get','install','rabbitmq-server','-y'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out,err) = child.communicate()
    logger.info(out)
    if err:
        logger.error(err)
    subprocess.check_call('rabbitmqctl add_vhost %s'%mq_host,shell=True)
    subprocess.check_call('rabbitmqctl add_user %s %s'%(mq_host,mq_pass),shell=True)
    subprocess.check_call('rabbitmqctl set_permissions -p "%s" %s ".*" ".*" ".*"'%(mq_user,mq_host),shell=True)
    subprocess.check_call('rabbitmqctl set_user_tags %s administrator'%mq_user,shell=True)
    

def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        logger.info('++++++++++++++ start install_mq ++++++++++++++++++')
        install_mq()
        os.mknod(lockfile)
        logger.info('++++++++++++++ end install_mq ++++++++++++++++++')


if __name__ == "__main__":
    run()
