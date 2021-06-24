import requests
from lxml import etree
from fake_useragent import UserAgent
import random

class selling_24h():

    STATUS = ''
    ITEMS = dict()

    @classmethod
    def get_24h(cls, ip, url):
        ua = UserAgent()
        list = random.choice(ip)

        proxy = {'https': 'https://' + list.ip_address + ':' + list.ip_port}
        header = {"user-agent": ua.random}
        req = requests.get(url, headers=header, proxies=proxy)
        if req.status_code != 200:
            return '当当网爬取失败'
        txt = etree.HTML(req.text)

        id_1 = txt.xpath("//li/div[1]/text()")
        book_name = txt.xpath("//div[2]/ul/li/div[3]/a/text()")
        img = txt.xpath("//div[@class='pic']/a/img/@src")
        comments_1 = txt.xpath("//div[@class='star']/a/text()")
        recommended_1 = txt.xpath("//div[@class='star']/span/text()")
        author = txt.xpath("//ul/li/div[5]/a[1]/text()")
        date = txt.xpath("//div[@class='publisher_info']/span/text()")
        publishing = txt.xpath("//div[@class='publisher_info'][2]/a/text()")
        price_1 = txt.xpath("//div[@class='price']/p/span[1]/text()")
        url = txt.xpath("//li/div[@class='name']/a/@href")

        id = []
        price = []
        comments = []
        recommended = []

        for i in range(len(id_1)):
            id.append(id_1[i].strip('.'))
            price.append((price_1[i].strip('¥')))
            comments.append(comments_1[i].strip('条评论'))
            recommended.append(recommended_1[i].strip('推荐'))

        cls.ITEMS = {
            'id': id, 'book_name': book_name, 'img': img, 'comments': comments, 'recommended': recommended,
            'author': author, 'date': date, 'publishing': publishing, 'price': price, 'url': url
        }
