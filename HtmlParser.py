#!/usr/bin/env python
# encoding: utf-8
"""
@author: jinlinfang
@contact: crawler_jinlinfang@163.com
@file: HtmlParser.py
@time: 7/25/18 1:28 PM
"""
import numpy, pandas, re, subprocess, os,urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
	def parser(self, page_url,html_cont):
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls, new_data
	def _get_new_urls(self, page_url,soup):
		new_urls = set()
		links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return  new_urls

	def _get_new_data(self, page_url, soup):
		data = {}
		data['url'] = page_url
		title = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
		data['title'] = title.get_text()
		summary = soup.find('div', class_='lemma-summary')
		data['summary'] = summary.get_text()
		return data



