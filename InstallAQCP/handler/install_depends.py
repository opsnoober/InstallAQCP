def run():
    print "install_depends+++++++++++++++++++"

import sys
import os
import shutil
import subprocess
sys.path.append('../')
from utils.add_log import add_log

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','install_depends.lck')
deps_list = ['gcc','g++','make','zip','unzip','lrzsz','python-pip','python-dev']

def install_deps():
    for dep_pkg in deps_list:
        subprocess.call(['apt-get','-y','install',dep_pkg])
    

@add_log(__name__)
def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        install_deps()

if __name__ == "__main__":
    run()
