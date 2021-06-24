import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from fake_useragent import UserAgent
from sql_model.dangdang import dang_model
import random

class Hot_Seach():

    @classmethod
    def seach_spider(cls, app, ip):
        db = dang_model.db
        db.init_app(app)
        pra = dang_model.HotSearch.query.delete()
        print(pra)
        db.session.commit()

        ops = ChromeOptions()
        ua = UserAgent()
        lis = random.randint(0,len(ip))
        proxy =  'http://' + ip[lis].address

        print(proxy)
        ops.add_argument('–-proxy-server=%s' % proxy)
        ops.add_argument('--user-agent=%s' % ua.random)
        url = "http:/bang.dangdang.com/books/hotbang"
        driver = webdriver.Chrome(options=ops)
 
        driver.get(url)
        time.sleep(0.5)
        name = driver.find_elements_by_xpath("//div[@class='bang-title']/span")
        out = driver.find_elements_by_tag_name("output")
        book_name = []

        for i in range(len(out)):
            print(out[i].text)
            n = name[i].text.strip('# ')
            book_name.append(n)
            hot = dang_model.HotSearch(id=i+1, name=book_name[i], popularity=out[i].text)
            db.session.add(hot)
            db.session.commit()

        db.session.close()
        driver.close()