#!/usr/bin/env python
# encoding: utf-8
"""
@author: jinlinfang
@contact: crawler_jinlinfang@163.com
@file: HtmlDownloader.py
@time: 7/25/18 2:10 PM
"""
import numpy, pandas, re, subprocess, os


class HtmlDownloader(object):
	def download(self,url):
		if url is None:
			return None
