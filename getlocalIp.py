# encoding:utf-8
import os
import sys
import time
import socket
import subprocess
import requests

upload_ip_url = r"http://106.12.129.87:5000/j4u/raspberry/localIp"


def getLocalIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('114.114.114.114', 0))
        ip = s.getsockname()[0]
    except:
        name = socket.gethostname()
        ip = socket.gethostbyname(name)
    if ip.startswith("127."):
        cmd = '''/sbin/ifconfig | grep "inet " | cut -d: -f2 | awk '{print $1}' | grep -v "^127."'''
        a = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        a.wait()
        out = a.communicate()
        ip = out[0].strip().split("\n")  # 所有的列表
        if len(ip) == 1 and ip[0] == "" or len(ip) == 0:
            return False
        ip = "over".join(ip)
    return ip


def upload_ip(ip):
    params = {'ip': ip}
    requests.get(upload_ip_url, params)


if '__main__' == __name__:
    upload_ip(getLocalIP())
