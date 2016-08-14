#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import re
import os
from bs4 import BeautifulSoup

class PageHandler:
    def __init__(self, url, authheader = None):
        self.url = url
        self.authheader = authheader
        self.url_req = urllib2.Request(url)
        self.cur_dir = os.getcwd()
        if self.authheader != None:
            self.url_req.add_header("Authorization", authheader)
            self.url_req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')


    def open_page(self):
        self.url_handler = urllib2.urlopen(self.url_req)


    def read_page(self):
        self.open_page()
        return self.url_handler.read()


    def download_page(self):
    	print 'download'
        pass


    def analysis_page(self):
    	self.page_soup = BeautifulSoup(self.read_page(),"html.parser")

    	# find all link
    	self.url_list = self.page_soup.find_all('a')
    	
    	# link iteration
    	for link in self.url_list:
    		link_url = "http://linux.linuxidc.com" + link.get('href')
    	
    		# match directory
    		regex_pattern = r'.\..'
    		pattern = re.compile(regex_pattern)
    		text = link.get_text()
    		text_match = re.findall(regex_pattern, text)
    	
    		# current directory has files
    		if text_match:
    			self.download_page()
    		elif text == '[To Parent Directory]':
    			pass
    		else: # get a new page
    			self.change_dir(text)
    			new_pagehandler = PageHandler(link_url, self.authheader)
    			try:
    				new_pagehandler.analysis_page()
    			except IOError, e:
    				print e
    				pass
    			finally:
    				os.chdir(self.cur_dir)
    		# print link_url
    		#print text
    		


    def change_dir(self, link_text):
    	cwd = os.getcwd()
    	new_dir = unicode(cwd) + u'/' + link_text

    	try:
    		os.chdir(new_dir)
    	except OSError, e:
    		os.mkdir(new_dir)
    		os.chdir(new_dir)
    	finally:
    		# print os.getcwd()
    		pass
    	

if __name__ == '__main__':
    pass
