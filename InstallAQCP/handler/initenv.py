import sys
import os
sys.path.append('../')
from utils.add_log import add_log

basedir = os.path.split(os.path.realpath(__file__))[0] 
lockfile = os.path.join(os.path.dirname(basedir),'lock','initenv.lck')
def sudoenv():
    sudo_nopass = '''
secneo ALL=NOPASSWD: /home/secneo/bangcle/scripts/update_vdb.sh
secneo ALL=NOPASSWD: /etc/init.d/csam restart
secneo ALL=NOPASSWD: /etc/init.d/csam start
secneo ALL=NOPASSWD: /sbin/initctl restart network-interface INTERFACE=em1
secneo ALL=NOPASSWD: /sbin/initctl restart network-interface INTERFACE=eth0
'''
    if os.path.exists(lockfile):
        print "You can only run this part once time"
        sys.exit(1)
    else:
        with open('/etc/sudoers','a') as f:
            f.write(sudo_nopass)
            f.write('\n')
        os.mknod(lockfile)
        os.system('chown secneo. /etc/network/interfaces')
        return 

@add_log(__name__)
def run():
    sudoenv()

if __name__ == "__main__":
    run()
