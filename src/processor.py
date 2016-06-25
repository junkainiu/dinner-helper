# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class HtmlProcessor(object):

    def __init__(self, doc):
        self.doc = doc
        self.root = ''


class LihuaProcessor(object):

    def process(self):
        soup = BeautifulSoup(self.doc)
        with open('lihua.html', 'w') as fp:
            fp.write(soup)
        return soup
