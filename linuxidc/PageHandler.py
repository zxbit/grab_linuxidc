#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import re
import bs4

class PageHandler:
    def __init__(self, url, authheader=None):
        self.url = url
        self.authheader = authheader
        self.url_req = urllib2.Request(url)
        if self.authheader != None:
            self.url_req.add_header("Authorization", authheader)

    def open_page(self):
        self.url_handler = urllib2.urlopen(self.url_req)

    def read_page(self):
        self.open_page()
        print self.url_handler.read()

    def download_page(self):
        pass

if __name__ == '__main__':
    pass
