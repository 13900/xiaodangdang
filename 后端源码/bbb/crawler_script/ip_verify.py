import requests
from fake_useragent import UserAgent
from crawler_script.ip_del import Delete_Ip

class Verify():

    URL1 = 'https://www.baidu.com/'
    URL2 = 'https://cn.bing.com/'

    VY = True
    @classmethod
    def req_ip(cls, app, ip_dats):
        vy = cls.VY
        ua = UserAgent()
        header = {"User-Agent": ua.random}
        ip = 'https://' + ip_dats
        proxy = {'ipaddr': ip}

        try:
            if  requests.get(cls.URL2, headers=header, proxies=proxy, verify=True, timeout=0.5).status_code == 200:
                print('这是存活IP-->', proxy['ipaddr'])
                vy = True
            else:
                if requests.get(cls.URL2, headers=header, proxies=proxy, verify=True, timeout=0.5).status_code == 200:
                    print('这是存活IP-->', proxy['ipaddr'])
                    vy = True
                else:
                    Delete_Ip.del_ip(app, ip=ip_dats)
                    vy = False
                    return '这IP已失效' + proxy['ipaddr']
            print('这是存活IP-->', proxy)
        except requests.exceptions.RequestException as e:
            Delete_Ip.del_ip(app=app, ip=ip_dats)
            vy = False
            print('此IP连接超时===》' + proxy['ipaddr'])
            print(e)

        return vy


