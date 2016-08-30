import sys
import os
import shutil
import subprocess
import time
sys.path.append('../')
from utils.log import Logger

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_depends.lck')
logger = Logger(logname=os.path.join(os.path.dirname(basedir),'logs','install.log'),loglevel=
1,logger='install_depends').getlog()
apt_deps_list = [
'lib32z1',
'lib32ncurses5',
'lib32bz2-1.0',
'expect',
'zlib1g-dev',
'python-mysqldb',
'libxml2:i386',
'libxslt-dev',
'cl-cffi',
'libffi-dev',
'libpango1.0-0',
'python-imaging',
'python-twisted',
'libwww-perl',
'rpm',
'dos2unix',
'python-protobuf',
'libreoffice',
'unoconv',
'xfonts-intl-chinese',
'xfonts-wqy',
'ttf-wqy-zenhei',
'ttf-wqy-microhei',
'xfonts-intl-chinese-big'
]
pip_conf = os.path.join(os.path.dirname(basedir),'settings','pip.conf')

def install_apt_deps():
    for apt_dep_pkg in apt_deps_list:
        child = subprocess.Popen(['apt-get','-y','install',apt_dep_pkg],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        (out,err) = child.communicate()
        logger.info(out)
        if err:
            logger.error(err)
def install_pip_deps():
    try:
        os.makedirs('/root/.pip')
    except:
        pass
    shutil.copy(pip_conf,'/root/.pip/pip.conf')
#############install pypiserver
    child1 = subprocess.Popen(['pip','install',os.path.join(os.path.dirname(basedir),'libs','pips','pypiserver-1.1.10-py2.py3-none-any.whl')],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out1,err1) = child1.communicate()
    logger.info(out1)
    if err1:
        logger.error(err1)
############# run pypiserver
    subprocess.Popen(['pypi-server','-p','7001',os.path.join(os.path.dirname(basedir),'libs','pips')])
   #time.sleep(3)
##############install pip pkgs
    logger.info('-------------------start install pip pkgs--------------------------------')
    child2 = subprocess.Popen(['pip','install','-r',os.path.join(os.path.dirname(basedir),'settings','requirement.txt'),'-i','http://127.0.0.1:7001/simple/'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (out2,err2) = child2.communicate()
    logger.info(out2)
    if err2:
        logger.error(err2)
    
    logger.info('------------------finish install pip pkgs--------------------------------')

def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        logger.info('++++++++++++++ start install_depends ++++++++++++++++++')
        install_apt_deps()
        install_pip_deps()
        os.mknod(lockfile)
        logger.info('++++++++++++++ end install_depends ++++++++++++++++++')

if __name__ == "__main__":
    run()
