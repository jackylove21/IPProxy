# coding: utf-8

import requests
from lxml import etree
from datetime import datetime


class Ip181Proxy(object):
    def __init__(self):
        self.url = 'http://www.ip181.com/'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/27.0.1453.90 Safari/537.36'}

    def get_ip(self, url):
        r = requests.get(url, headers=self.headers)
        html = etree.HTML(r.content)
        all_ip = html.xpath('//table//tr[not(@class="active")]')
        for i in all_ip:
            ip = i.xpath('./td[1]/text()')[0]
            port = i.xpath('./td[2]/text()')[0]
            country = i.xpath('./td[6]/text()')[0]
            anonymous = i.xpath('./td[3]/text()')[0]
            http_type = i.xpath('./td[4]/text()')[0]
            speed=i.xpath('td[5]/text()')[0]
            from_site = 'ip181'
            crawl_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print('-----', ip, port, country, anonymous, http_type, from_site, crawl_time, '=====')
            proxy = (ip, port, country, anonymous, http_type,speed, from_site)
            yield proxy

    def start(self):
        for proxy in self.get_ip(self.url):
            yield proxy


if __name__ == '__main__':
    p = Ip181Proxy()
    for p_ip in p.start():
        print(p_ip)
