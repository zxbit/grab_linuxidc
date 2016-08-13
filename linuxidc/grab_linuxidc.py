#! /usr/bin/python
# encoding:utf-8

import urllib2
import sys
import re
from urlparse import urlparse
import base64

url = 'http://linux.linuxidc.com'
username = 'www.linuxidc.com'
password = 'www.linuxidc.com'

base64string = base64.encodestring('%s:%s' %(username, password))[:-1]
authheader = "Basic %s" % base64string

url_req = urllib2.Request(url)
url_req.add_header("Authorization", authheader)

try:
    url_handle = urllib2.urlopen(url_req)
except IOError, e:
    print e

url_text = url_handle.read()
print url_text
