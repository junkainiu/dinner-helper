# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class HtmlProcessor(object):

    def __init__(self, doc):
        self.doc = doc


class LihuaProcessor(object):

    def process(self):
        soup = BeautifulSoup(self.doc)
        return soup
