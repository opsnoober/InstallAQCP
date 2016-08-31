import sys
import os
import shutil
import subprocess
sys.path.append('../')
from utils.log import Logger
from utils.config import Get_data

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_mysql.lck')
logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=
1,logger='install_mysql').getlog()
getdata = Get_data(os.path.join(os.path.dirname(basedir),'conf.ini'))
db_pass = getdata.Show_option_data('db','db_pass')


def install_mysql():
    cmd1 = "echo 'mysql-server-5.5 mysql-server/root_password password %s'|debconf-set-selections"%db_pass
    cmd2 = "echo 'mysql-server-5.5 mysql-server/root_password_again password %s'|debconf-set-selections"%db_pass
    subprocess.check_call(cmd1,shell=True)
    subprocess.check_call(cmd2,shell=True)
    child = subprocess.Popen(['apt-get','install','mysql-server','-y'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out,err) = child.communicate()
    logger.info(out)
    if err:
        logger.error(err)
    

def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        logger.info('++++++++++++++ start install_mysql ++++++++++++++++++')
        install_mysql()
        os.mknod(lockfile)
        logger.info('++++++++++++++ end install_mysql ++++++++++++++++++')


if __name__ == "__main__":
    run()
