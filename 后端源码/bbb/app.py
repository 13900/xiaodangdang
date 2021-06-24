import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from my_error.APIException import APIException
from my_error.errorcode import ServerError
import jwt
from jwt import exceptions
import datetime
import os
from crawler_script.ip_crawler import Ip_Proxy
from confing import sql_conf
from sql_model import ip_model, data_model
from sql_model.dangdang import dang_model
from crawler_script.ip_verify import Verify
from crawler_script.ip_del import Delete_Ip
from crawler_script.dangdang.praise_list import praise_list
from crawler_script.dangdang.hot_seach import Hot_Seach
from crawler_script.dangdang.Internet import Internet
from crawler_script.dangdang.literature import Literature
from crawler_script.dangdang.children import Children
from crawler_script.dangdang.natural_sciences import Natural_Sciences


app = Flask(__name__)
app.config.from_object(sql_conf)
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, supports_credentials=True)


@app.before_request
def af_req():
    try:
        if request.path == '/login' or request.path == '/registered':
            print('登陆开始')
        else:
            if (request.headers['authorization'] != '' or request.headers['authorization'] != None):
                token = request.headers['authorization']
                print(token)
                try:
                    jj = jwt.decode(token, app.config['SECRET_KEY'], issuer='potato', algorithms='HS256')
                    print(jj)
                except exceptions.ExpiredSignatureError:
                    print('token已经失效')
                    return '403'
                except jwt.DecodeError as e:
                    print('token认证失败')
                    print(e)
                    return '403'
                except jwt.InvalidTokenError:
                    print('非法的token')
                    return '403'
                print(request.path)
                print('0000000')
            else:
                return 404
    except exceptions:
        print(exceptions)
        return exceptions

@app.errorhandler(Exception)
def framework_error(e):
    # 判断异常是不是APIException
    if isinstance(e, APIException):
        return e
    # 判断异常是不是HTTPException
    if isinstance(e, HTTPException):
        code = e.code
        # 获取具体的响应错误信息
        msg = e.description
        return APIException(code=code, msg=msg)
    # 异常肯定是Exception
    else:
        return ServerError()


@app.route('/registered', methods=['POST'])
def registered():
    db = data_model.db
    db.init_app(app)
    db.create_all()
    ip_model.db.init_app(app)
    ip_model.db.create_all()
    dang_model.db.init_app(app)
    dang_model.db.create_all()
    user = data_model.user(email=request.json.get('email'), password=request.json.get('password'))
    db.session.add(user)
    db.session.commit()
    return '注册成功'


@app.route('/login', methods=['POST'])
def login():
    db = data_model.db
    db.init_app(app)
    email = request.json.get('email')
    password = request.json.get('password')
    if (email != '' and email != None and password != '' and password != None):
        user = data_model.user.query.filter(data_model.user.email == email, data_model.user.password == password)
        if (user != '' and user != None):
            dic = {
                'exp': datetime.datetime.now() + datetime.timedelta(days=1),
                'iss': 'potato',
                'iat': datetime.datetime.now(),
                'iss': 'potato',
                'data': {
                    'a': str(datetime.datetime.now()),
                    'b': 2,
                    'user': email
            }
        }
        code = jwt.encode(dic, app.config['SECRET_KEY'], algorithm='HS256')
    return code



@app.route('/ip/add', methods=['GET'])
def ip_add():
    print('ip爬虫开始')
    Ip_Proxy.Reurl(app)
    return 'IP爬虫成功'

# ip查询
@app.route('/ip/Inquire', methods=['GET'])
def ip_inquire():
    ip_model.db.__init__(app)
    ip_database = ip_model.ip_database
    ip = ip_database.query.limit(15).all()

    msg = []
    for i in range(len(ip)):
        vy = Verify.req_ip(app, ip[i].address)
        if vy:
            dat = {
                'name': ip[i].address,
                'AgentType': ip[i].types,
                'AgentLocation': ip[i].location
            }
            msg.append(dat)
    return jsonify(msg)

@app.route('/ip/del', methods=['POST'])
def ip_del():
    print('ip开始删除')
    ip = request.json.get('address')
    print(ip)
    print(request)
    Delete_Ip.del_ip(app=app, ip=ip)
    return 'ip删除成功'


# 蜘蛛
@app.route('/dangdang/hot_spider', methods=['GET'])
def hot():
    ip_model.db.__init__(app)
    ip_database = ip_model.ip_database
    ip = ip_database.query.limit(15).all()
    Hot_Seach.seach_spider(app=app, ip=ip)
    return '当当热搜榜爬取成功'

@app.route('/dangdang/praise_spdier', methods=['GET'])
def praise():
    ip_model.db.__init__(app)
    ip_database = ip_model.ip_database
    ip = ip_database.query.limit(15).all()
    praise_list.Praise_spider(app=app, ip=ip)
    return '当当好评榜爬取成功'

@app.route('/dangdang/internet_spider', methods=['GET'])
def internet_spider():
    ip_model.db.__init__(app)
    ip_database = ip_model.ip_database
    ip = ip_database.query.limit(35).all()
    Internet.internet_spider(app=app, ip=ip)
    return '当当互联网·IT榜爬取成功'

@app.route('/dangdang/literature_spider', methods=['GET'])
def literature_spider():
    ip_model.db.__init__(app)
    ip_database = ip_model.ip_database
    ip = ip_database.query.limit(35).all()
    Literature.literature_spider(app=app, ip=ip)
    return '当当文学榜爬取成功'

@app.route('/dangdang/children_spider', methods=['GET'])
def children_spider():
    ip_model.db.__init__(app)
    ip_database = ip_model.ip_database
    ip = ip_database.query.limit(35).all()
    Children.children_spider(app=app, ip=ip)
    return '当当童书榜爬取成功'

@app.route('/dangdang/natural_sciences_spider', methods=['GET'])
def parentchild_spider():
    ip_model.db.__init__(app)
    ip_database = ip_model.ip_database
    ip = ip_database.query.limit(35).all()
    Natural_Sciences.Natural_Sciences_spider(app=app, ip=ip)
    return '当当自然科学榜爬取成功'

#数据返回
@app.route('/all/data', methods=['GET'])
def all_date():
    ip_model.db.__init__(app)
    dang_model.db.__init__(app)

    hotList = dang_model.HotSearch.query.count()
    internet = dang_model.Internet.query.count()
    literature = dang_model.Literature.query.count()
    children = dang_model.Children.query.count()
    nal = dang_model.Natural_Sciences.query.count()
    ip = ip_model.ip_database.query.count()
    msg = {
        'sum': hotList+internet+literature+children+nal,
        'ip': ip
    }

    return jsonify(msg)


@app.route('/dangdang/prase', methods=['GET'])
def praise_li():
    db = dang_model.db
    db.init_app(app)
    pra = dang_model.Praise.query.limit(5).all()
    id = []
    comment = []
    good_comment = []
    variance = []
    dat = []
    for i in range(len(pra)):
        id.append(pra[i].id)
        comment.append(pra[i].comment)
        good_comment.append(pra[i].good_comment)
        variance.append((int(comment[i]) - int(good_comment[i])))
    print(variance)
    dat.append(id)
    dat.append(comment)
    dat.append(good_comment)
    dat.append(variance)
    return jsonify(dat)

@app.route('/dangdang/hotList')
def hot_list():
    db = dang_model.db
    db.init_app(app)
    hot = dang_model.HotSearch.query.limit(5).all()
    print(type(hot))
    dat  = []
    for i in range(len(hot)):
        msg = {
        'value': hot[i].popularity,
        'name': hot[i].name
        }
        dat.append(msg)
    return jsonify(dat)

@app.route('/dangdang/internet', methods=['GET'])
def internet():
    page = int(request.args.get('page'))
    print('page')
    print(page)
    value1 = 20 * page
    value2 = 20
    print(type(value1), type(value2))
    ip_model.db.__init__(app)
    be_mo = dang_model.Internet.query.limit(value2).offset(value1).all()
    msg = dang_data_format(be_mo=be_mo)

    return jsonify(msg)

@app.route('/dangdang/literature', methods=['GET'])
def literature():
    page = int(request.args.get('page2'))

    value1 = 20 * page
    value2 = 20
    ip_model.db.__init__(app)
    be_mo = dang_model.Literature.query.limit(value2).offset(value1).all()
    msg = dang_data_format(be_mo=be_mo)
    return jsonify(msg)

@app.route('/dangdang/children', methods=['GET'])
def children():
    page = int(request.args.get('page3'))

    value1 = 20 * page
    value2 = 20
    ip_model.db.__init__(app)
    be_mo = dang_model.Children.query.limit(value2).offset(value1).all()
    msg = dang_data_format(be_mo=be_mo)
    return jsonify(msg)

@app.route('/dangdang/natural_sciences', methods=['GET'])
def parent_child():
    page = int(request.args.get('page4'))

    value1 = 20 * page
    value2 = 20
    ip_model.db.__init__(app)
    be_mo = dang_model.Natural_Sciences.query.limit(value2).offset(value1).all()
    msg = dang_data_format(be_mo=be_mo)
    return jsonify(msg)

def dang_data_format(be_mo):
    color = ['#952175', '#1F7087', '#C71585', '#6A5ACD', '#008B8B', '#6B8E23', '#DAA520', '#BC8F8F', '#808000']
    msg = []
    for i in range(len(be_mo)):
        col = random.choice(color)
        dat = {
            'color': col,
            'id': be_mo[i].rank,
            'src': be_mo[i].img,
            'url': be_mo[i].url,
            'chip': '当当网',
            'title': be_mo[i].bo_na,
            'name': be_mo[i].name,
            'artist': be_mo[i].publishing,
            'show': False,
            'dialog': False,
            'option': {
                'title': {
                    'text': '价格表',
                    'color': '#81C784'
                },
                'tooltip': {
                    'trigger': 'axis'
                },
                'xAxis': {
                    'type': 'category',
                    'data': ['原价', '电子书价格', '打折价']
                },
                'yAxis': {
                    'type': 'value'
                },
                'series': [{
                    'data': [be_mo[i].ori_price, be_mo[i].ebook, be_mo[i].price],
                    'type': 'bar',
                    'showBackground': 'true',
                    'backgroundStyle': {
                        'color': 'rgba(220, 220, 220, 0.8)'
                    }
                }]
            }
        }
        msg.append(dat)
    return msg

if __name__ == '__main__':
    app.run()
