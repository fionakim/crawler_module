#!/usr/bin/env python
# encoding: utf-8
"""
@author: jinlinfang
@contact: crawler_jinlinfang@163.com
@file: DataOutput.py
@time: 7/25/18 1:57 PM
"""
import numpy, pandas, re, subprocess, os,codecs

class DataOutput(object):
	def __init__(self):
		self.datas = []
	def store_data(self,data):
		if data is None:
			return
		self.datas.append(data)
	def out_html(self):
		fout = codecs.open("baike.html",'w',encoding='utf-8')
		fout.write()