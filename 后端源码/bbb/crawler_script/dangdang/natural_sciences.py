import requests
from lxml import etree
from fake_useragent import UserAgent
from sql_model.dangdang import dang_model
import random

class Natural_Sciences():

    @classmethod
    def Natural_Sciences_spider(cls, app, ip):
        page = 1

        db = dang_model.db
        db.init_app(app)
        pra = dang_model.Natural_Sciences.query.delete()
        print(pra)
        db.session.commit()
        while True:
            ua = UserAgent()
            lis = random.randint(1, len(ip)-1)
            proxy = {'ipaddr': 'http://' + ip[lis].address}
            header = {"user-agent": ua.random}

            req = requests.get('http://bang.dangdang.com/books/bestsellers/01.62.00.00.00.00-24hours-0-0-1-%d'%page,
                           headers=header, proxies=proxy)
            if req.status_code != 200:
                print(req.status_code)
                print('当当网好评榜爬取失败')
                return '当当网好评榜爬取失败'

            txt = etree.HTML(req.text)
            id = txt.xpath("//div/ul[@class='bang_list clearfix bang_list_mode']/li/div[1]/text()")
            bo_na = txt.xpath("//div/ul[@class='bang_list clearfix bang_list_mode']/li/div[3]/a/text()")
            name = txt.xpath("//div/ul[@class='bang_list clearfix bang_list_mode']/li/div[5]/a[1]/text()")
            publishing = txt.xpath("//div/ul[@class='bang_list clearfix bang_list_mode']/li/div[6]/a[1]/text()")
            price = txt.xpath("//div/ul[@class='bang_list clearfix bang_list_mode']/li/div[7]/p[1]/span[1]/text()")
            original_price = txt.xpath("//div/ul[@class='bang_list clearfix bang_list_mode']/li/div[7]/p[1]/span[2]/text()")
            url = txt.xpath("//div/ul[@class='bang_list clearfix bang_list_mode']/li/div[3]/a/@href")
            img = txt.xpath("//div[@class='pic']/a/img/@src")
            ebook_price = []
            if page is 1 or page is None:
                pa = txt.xpath("//ul[@name='Fy']/li[last()-2]/a/text()")
                pa = int(pa[0])


            for i in range(len(id)):

                ebook = txt.xpath("//div/ul[@class='bang_list clearfix bang_list_mode']/li[%d]"%(i+1)+"/div[7]/p[2]/span")
                if not ebook:
                    print('12')
                    price[i] = price[i].strip('¥')
                    original_price[i] = original_price[i].strip('¥')
                    bo_na[i] = bo_na[i].split('（', 1)[0]
                    ebook_price.append('0')
                    continue
                price[i] = price[i].strip('¥')
                original_price[i] = original_price[i].strip('¥')
                ebook_price.append(ebook[0].text.strip('¥'))
                bo_na[i] = bo_na[i].split('（', 1)[0]

            for i in range(len(name)):
                best = dang_model.Natural_Sciences(rank=id[i], name=name[i], bo_na=bo_na[i], url=url[i],
                                              publishing=publishing[i], price=price[i], ori_price=original_price[i],
                                              ebook=ebook_price[i], img=img[i])
                db.session.add(best)
                db.session.commit()

            page = page + 1
            pa = pa - 1
            print(pa)
            if pa == 0:
                return '0'

