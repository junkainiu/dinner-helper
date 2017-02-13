# -*- coding: utf-8 -*-
import urllib2
from processor import LihuaProcessor


class HtmlCollector(object):

    pass


class LihuaCollector(object):

    URL = "http://www.lihua.com"

    def connect(self):
        header = self.get_header()
        req = urllib2.Request(self.URL, headers=header)
        con = urllib2.urlopen(req)
        doc = con.read()
        result = LihuaProcessor(doc)
        con.close()

    def get_header(self):
        header = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": 0,
            "Cookie": "PHPSESSID=e386gmipdk3p6k7ltq7hqkg2u6; lihua_home__user_inv=%E4%B8%8A%E6%B5%B7%E5%A4%A9%E6%97%A6%E7%BD%91%E7%BB%9C%E7%A7%91%E6%8A%80%E5%8F%91%E5%B1%95%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; lihua_home_lihuashop_cookie_tag=1; lihua_home_lihuashop_cookie_sn=2016060413465216; lihua_home_lihuashop_cookie_amount=23; lihua_home___forward__=%2Findex.php%3Fs%3D%2FHelp%2Findex%2Ftype%2F7.html; cckf_track_112082_AutoInviteNumber=0; cckf_track_112082_ManualInviteNumber=0; CCKF_visitor_id_112082=749323679",
            "Host": "www.lihua.com",
            "Origin": "http://www.lihua.com",
            "Referer": "http://www.lihua.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
        return header
