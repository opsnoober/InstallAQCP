#!/usr/bin/env python
#-*-coding:utf-8-*-
'''程序主文件'''
import argparse
from handler import initenv
from handler import install_base
from handler import install_depends
from handler import install_jdk
from handler import install_andsdk
from handler import install_mq
from handler import install_mysql
from handler import install_engine
from handler import install_kav
from handler import install_avast
from handler import install_cyren
from handler import install_fsecure
from handler import install_web
from handler import install_adb
from handler import install_others
import sys
import os

modulelist = [
'initenv',
'install_base',
'install_depends',
'install_jdk',
'install_andsdk',
'install_mq',
'install_mysql',
'install_engine',
'install_kav',
'install_avast',
'install_cyren',
'install_fsecure',
'install_web',
'install_adb',
'install_others'
]

def parse_args():
    '''解析参数'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-m','--modules',dest="modules",nargs = "*",help="choose module")
    parser.add_argument('-a','--all',dest="is_all",action='store_true',default=False,help="choose all module")
    parser.add_argument('-l','--list',dest="modulelist",action='store_true',default=False,help="list all modules")
    args = parser.parse_args()
    return args

def main():
    p = parse_args()
    if p.modulelist:
        print 'You can choose these modules:'
        for x in modulelist:
            print ' '*4,x

    if p.is_all:
        '''执行所有安装步骤'''
        initenv.run()
        install_base.run()
        install_depends.run()
        install_jdk.run()
        install_andsdk.run()
        install_mq.run()
        install_mysql.run()
        install_engine.run()
        install_kav.run()
        install_avast.run()
        install_cyren.run()
        install_fsecure.run()
        install_web.run()
        install_adb.run()
        install_others.run()

    if p.modules:
        for m in p.modules:
	    #判断传入的模块合法性验证
            if m not in modulelist:
                print 'you can only choose these modules:'
                for x in modulelist:
                    print ' '*4,x
            elif m == 'initenv':
                initenv.run()
                pass
            elif m == 'install_base':
                install_base.run()
                pass
            elif m == 'install_depends':
                install_depends.run()
                pass
            elif m == 'install_jdk':
                install_jdk.run()
                pass
            elif m == 'install_andsdk':
                install_andsdk.run()
                pass
            elif m == 'install_mq':
                install_mq.run()
                pass
            elif m == 'install_mysql':
                install_mysql.run()
                pass
            elif m == 'install_engine':
                install_engine.run()
                pass
            elif m == 'install_kav':
                install_kav.run()
                pass
            elif m == 'install_avast':
                install_avast.run()
                pass
            elif m == 'install_cyren':
                install_cyren.run()
                pass
            elif m == 'install_fsecure':
                install_fsecure.run()
                pass
            elif m == 'install_web':
                install_web.run()
                pass
            elif m == 'install_adb':
                install_adb.run()
                pass
            elif m == 'install_others':
                install_adb.run()
                pass
               

if __name__ == "__main__":
    if os.environ['USER'] != 'root':
        print 'You must run this script with root !!!'
        sys.exit(1)
    if len(sys.argv) < 2:
        print '''
usage: python main.py [-h] [-m [MODULES [MODULES ...]]] [-a] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -m [MODULES [MODULES ...]], --modules [MODULES [MODULES ...]]
                        choose module
  -a, --all             choose all module
  -l, --list            list all modules
'''    
        sys.exit(1)
    else:   
        main()
