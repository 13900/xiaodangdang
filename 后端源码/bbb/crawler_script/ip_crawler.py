from sql_model import ip_model
from fake_useragent import UserAgent
from lxml import etree
import requests
import random


class Ip_Proxy():

    IP_POOL = [
        {'ipaddr': 'http://120.9.140.168:9999'},
        {'ipaddr': 'http://112.111.77.222:9999'},
        {'ipaddr': 'http://140.238.17.39:8118'},
        {'ipaddr': 'http://18.135.32.174:80'},
        {'ipaddr': 'http://89.187.177.107:80'},
        {'ipaddr': 'http://113.238.142.208:3128'},
        {'ipaddr': 'http://45.167.197.11:80'},
        {'ipaddr': 'http://58.220.95.115:80'},
        {'ipaddr': 'http://113.195.224.239:9999'},
        {'ipaddr': 'http://221.182.31.54:8080'},
    ]
    PAGE = '/gaoni/1/'
    COUNT = 0
    @classmethod
    def Reurl(cls, app):

        db = ip_model.db
        db.init_app(app)

        while True:

            ua = UserAgent()
            proxy = random.choice(cls.IP_POOL)
            header = {"user-agent": ua.random}

            req = requests.get('http://www.xiladaili.com'+ cls.PAGE, headers=header, proxies=proxy, timeout=5)
            if req.status_code < 200 or req.status_code > 300:
                print('爬虫出错啦')
                print(req.status_code)
                db.session.close()
                print('数据库关闭1')
                return '爬虫出错啦'
            txt = etree.HTML(req.text)
            ip_address = txt.xpath("//tr/td[1]//text()")
            ip_types = txt.xpath("//tr/td[2]//text()")
            ip_location = txt.xpath("//tr/td[4]//text()")

            for i in range(len(ip_address)):
                ip_data = ip_model.ip_database(address=ip_address[i], types=ip_types[i], location=ip_location[i])
                db.session.add(ip_data)
                db.session.commit()

            print(cls.COUNT)

            if cls.COUNT < 7:
                cls.PAGE = txt.xpath("//nav/ul/li[16]/a/@href")
                cls.PAGE = str(cls.PAGE).strip("['']")
                print(16)
            else:
                cls.PAGE = txt.xpath("//nav/ul/li[17]/a/@href")
                cls.PAGE = str(cls.PAGE).strip("['']")
                print(17)
            print(cls.PAGE == '' or cls.PAGE == None)
            if cls.PAGE == '' or cls.PAGE == None:
                print('爬虫结束')
                db.session.close()
                print('数据库关闭2')
                return 0
            print('开始翻页')
            print(cls.PAGE)
            cls.COUNT = cls.COUNT + 1




