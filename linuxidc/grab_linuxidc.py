#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import sys
import re
from urlparse import urlparse
from HTTPAuthorization import HTTPAuthorization
from PageHandler import PageHandler

# 根目录网址及用户名密码
url = 'http://linux.linuxidc.com'
username = 'www.linuxidc.com'
password = 'www.linuxidc.com'

# 创建授权header
httpauthorization = HTTPAuthorization(username, password)
authheader = httpauthorization.gen_authheader()

url_page = PageHandler(url,authheader)

try:
    url_page.read_page()
except IOError, e:
    print e


if __name__ == '__main__':
    pass
