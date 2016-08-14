#! /usr/bin/python
# -*- coding: utf-8 -*-

__metaclass__ = type

import base64

class HTTPAuthorization:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def gen_authheader(self):
        base64string = base64.encodestring('%s:%s' %(self.username, self.password))[:-1]
        self.authheader = "Basic %s" % base64string
        return self.authheader

if __name__ == '__main__':
    pass
