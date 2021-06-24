import requests
from lxml import etree
from fake_useragent import UserAgent
from sql_model.dangdang import dang_model
import random

class praise_list:

    @classmethod
    def Praise_spider(cls, app, ip):

        db = dang_model.db
        db.init_app(app)
        pra = dang_model.Praise.query.delete()
        print(pra)
        db.session.commit()


        ua = UserAgent()
        lis = random.randint(0,len(ip))
        proxy = {'ipaddr': 'http://' + ip[lis].address }
        header = {"user-agent": ua.random}

        req = requests.get('http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1', headers=header, proxies=proxy)
        if req.status_code != 200:
            print(req.status_code)
            print('当当网好评榜爬取失败')
            return '当当网好评榜爬取失败'

        txt = etree.HTML(req.text)
        id = txt.xpath("//ul[@class='bang_list clearfix bang_list_mode']/li/div[1]/text()")
        name = txt.xpath("//ul[@class='bang_list clearfix bang_list_mode']/li/div[@class='name']/a/text()")
        comment = txt.xpath("//ul[@class='bang_list clearfix bang_list_mode']/li/div[@class='star']/a/text()")
        good_comment = txt.xpath("//ul[@class='bang_list clearfix bang_list_mode']/li/div[@class='biaosheng']/span/text()")

        for i in range(len(id)):
            id[i] = id[i].strip('.')
            comment[i] = comment[i].strip('条评论')
            good_comment[i] = good_comment[i].strip('次')

            praise = dang_model.Praise(id=id[i], name=name[i], comment=comment[i], good_comment=good_comment[i])
            db.session.add(praise)
            db.session.commit()

        db.session.close()




