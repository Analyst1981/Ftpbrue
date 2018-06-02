#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import socks
import requests
import requesocks
import time
import os
'''


 
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050, True)
#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050, True, 'socks5_user','socks_pass')
socket.socket = socks.socksocket
a=requests.get('http://checkip.amazonaws.com').text
#print(requests.get('http://api.ipify.org?format=json').text)
print a

'''
url = 'http://api.ipify.org?format=json'


def getip_requests(url):
    print "(+) Sending request with plain requests..."
    r = requests.get(url)
    print "(+) IP is: " + r.text.replace("\n", "")                       

def getip_requesocks(url):
    print "(+) Sending request with requesocks..."
    session = requesocks.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'}
    r = session.get(url)
    print "(+) IP is: " + r.text.replace("\n", "")


def main():
    print "Running tests..."
    getip_requests(url)
    getip_requesocks(url)
    os.system("""(echo authenticate '"test1234"'; echo signal newnym; ) echo \
    quit| nc localhost 9051""") 
    time.sleep(10)
    getip_requesocks(url)


if __name__ == "__main__":
    main()
