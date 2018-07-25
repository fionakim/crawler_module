#!/usr/bin/env python
# encoding: utf-8
"""
@author: jinlinfang
@contact: crawler_jinlinfang@163.com
@file: UrlManager.py
@time: 7/25/18 1:27 PM
"""
import numpy, pandas, re, subprocess, os


class UrlManager(object):

	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	def has_new_url(self):
		'''
		judge wherther it has uncrawled url
		:return:
		'''
		return self.new_urls_size() != 0

	def new_urls_size(self):
		return len(self.new_urls)

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def add_new_url(self, url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def add_new_urls(self, urls):
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.add_new_url(url)

	def old_url_size(self):
		return len(self.old_urls)
