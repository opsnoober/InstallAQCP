import sys
import os
import shutil
import subprocess
sys.path.append('../')
from utils.add_log import add_log

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','initenv.lck')
apt_pkgs = os.path.join(os.path.dirname(basedir),'res','archives')
apt_sources_conf = os.path.join(os.path.dirname(basedir),'settings','sources.list')
apt_conf = os.path.join(os.path.dirname(basedir),'settings','apt.conf')

def conf_env():
    sudo_nopass = '''
secneo ALL=NOPASSWD: /home/secneo/bangcle/scripts/update_vdb.sh
secneo ALL=NOPASSWD: /etc/init.d/csam restart
secneo ALL=NOPASSWD: /etc/init.d/csam start
secneo ALL=NOPASSWD: /sbin/initctl restart network-interface INTERFACE=em1
secneo ALL=NOPASSWD: /sbin/initctl restart network-interface INTERFACE=eth0
'''
    profile_env = '''
export JAVA_HOME=/usr/local/jdk
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export ANDROID_HOME=/usr/android-sdk-linux/tools
export ANDROID_TOOL=/usr/android-sdk-linux/platform-tools
export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$ANDROID_HOME:$ANDROID_TOOL:$PATH
'''
    with open('/etc/sudoers','a') as f:
        f.write(sudo_nopass)
        f.write('\n')
    with open('/etc/profile','a') as f:
        f.write(profile_env)
        f.write('\n')

    os.mknod(lockfile)
    os.system('chown secneo. /etc/network/interfaces')

def conf_apt():
    os.rename("/etc/apt/sources.list","/etc/apt/sources.list.bak")
    try:
        os.mkdir('/debs')
    except OSError:
        pass
    shutil.copytree(apt_pkgs,'/debs/archives')
    shutil.copy(apt_sources_conf,'/etc/apt/sources.list')
    shutil.copy(apt_conf,'/etc/apt/apt.conf')
    subprocess.call(['apt-get','update'])

@add_log(__name__)
def run():
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        conf_env()
        conf_apt()

if __name__ == "__main__":
    run()
