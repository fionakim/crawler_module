#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function

"""
@author: jinlinfang
@contact: crawler_jinlinfang@163.com
@file: SpiderMan.py
@time: 7/25/18 1:16 PM
"""
import numpy, pandas, re, subprocess, os
from DataOutput import DataOutput
from HtmlParser import HtmlParser
from UrlManager import UrlManager
from HtmlDownloader import HtmlDownloader


class SpiderMan(object):
	def __init__(self):
		self.manager = UrlManager()
		self.downloader = HtmlDownloader()
		self.parser = HtmlParser()
		self.output=DataOutput()

		pass
	def crawl(self,root_url):
		self.manager.add_new_url(root_url)
		while (self.manager.has_new_url() and self.manager.old_url_size() <100):
			try:
				new_url = self.manager.get_new_url()
				html = self.downloader.download(new_url)
				new_urls,data = self.parser.parser(new_url,html)
				self.manager.add_new_url(new_urls)
				self.output.store_data(data)
				print()
			except Exception as e:
				print('crawl failed: '+e)

		self.output.out_html()

if __name__ == '__main__':
	man = SpiderMan()
	man.crawl("https://baike.baidu.com/view/284853.htm")