import sys
import os
import shutil
import subprocess
import time
sys.path.append('../')
from utils.add_log import add_log

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_depends.lck')
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
extra_deps_list = ['drozer_2.3.3.deb']
pip_conf = os.path.join(os.path.dirname(basedir),'settings','pip.conf')

def install_apt_deps():
    for apt_dep_pkg in apt_deps_list:
        subprocess.call(['apt-get','-y','install',apt_dep_pkg])
    for e_dep_pkg in extra_deps_list:
        subprocess.call(['dpkg','-i',os.path.join(os.path.dirname(basedir),'libs','extra',e_dep_pkg)])
    
def install_pip_deps():
    try:
        os.makedirs('/root/.pip')
    except:
        pass
    shutil.copy(pip_conf,'/root/.pip/pip.conf')
#############install pypiserver
    subprocess.call(['pip','install',os.path.join(os.path.dirname(basedir),'libs','pips','pypiserver-1.1.10-py2.py3-none-any.whl')])
############# run pypiserver
    subprocess.Popen(['pypi-server','-p','7001',os.path.join(os.path.dirname(basedir),'libs','pips')])
    time.sleep(3)
##############install pip pkgs
    subprocess.call(['pip','install','-r',os.path.join(os.path.dirname(basedir),'settings','requirement.txt'),'-i','http://127.0.0.1:7001/simple/'])
    

@add_log(__name__)
def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        install_apt_deps()
        install_pip_deps()
        os.mknod(lockfile)

if __name__ == "__main__":
    run()
