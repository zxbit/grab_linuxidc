#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import sys
import re
from urlparse import urlparse
from HTTPAuthorization import HTTPAuthorization
from PageHandler import PageHandler

# 根目录网址及用户名密码
url = r'http://linux.linuxidc.com/2011%E5%B9%B4%E8%B5%84%E6%96%99/Android%E5%85%A5%E9%97%A8%E6%95%99%E7%A8%8B/Android%E7%9A%84binder%E6%9C%BA%E5%88%B6%E7%A0%94%E7%A9%B6%EF%BC%88C++%E9%83%A8%E5%88%86%EF%BC%89/'
username = 'www.linuxidc.com'
password = 'www.linuxidc.com'

# 创建授权header
httpauthorization = HTTPAuthorization(username, password)
authheader = httpauthorization.gen_authheader()

url_page = PageHandler(url,authheader)

try:
    url_page.read_page()
except IOError, e:
    #print e
    pass


if __name__ == '__main__':
    pass
