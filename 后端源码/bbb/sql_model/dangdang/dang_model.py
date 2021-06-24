from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Praise(db.Model):
    __tablename__ = 'praise'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="好评榜排名")
    name = db.Column(db.String(100), nullable=False, comment="书名")
    comment = db.Column(db.String(30), nullable=False, comment="评论总评次数")
    good_comment = db.Column(db.String(30), nullable=False, comment="五星好评次数")

class HotSearch(db.Model):
    __tablename__ = 'hotSearch'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="热搜榜排名")
    name = db.Column(db.String(100), nullable=False, comment="书名")
    popularity = db.Column(db.String(30), nullable=False, comment="热搜人气")

class   Internet(db.Model):

    __tablename__ = 'Internet'

    rank = db.Column(db.Integer, primary_key=True, comment="IT*互联网排名")
    name = db.Column(db.String(100), nullable=False, comment="作者")
    bo_na = db.Column(db.String(100), nullable=False, comment="书名")
    url = db.Column(db.String(250), nullable=False, comment="图书地址")
    publishing = db.Column(db.String(30), nullable=False, comment="出版社")
    price = db.Column(db.String(30), nullable=False, comment="购买实价")
    ori_price = db.Column(db.String(30), nullable=False, comment="原价")
    ebook = db.Column(db.String(30), nullable=False, comment="电子书价格")
    img = db.Column(db.String(250), nullable=False, comment="图书封面")

class Literature(db.Model):

    __tablename__ = 'literature'

    rank = db.Column(db.Integer, primary_key=True, comment="文学排名")
    name = db.Column(db.String(100), nullable=False, comment="作者")
    bo_na = db.Column(db.String(100), nullable=False, comment="书名")
    url = db.Column(db.String(250), nullable=False, comment="图书地址")
    publishing = db.Column(db.String(30), nullable=False, comment="出版社")
    price = db.Column(db.String(30), nullable=False, comment="购买实价")
    ori_price = db.Column(db.String(30), nullable=False, comment="原价")
    ebook = db.Column(db.String(30), nullable=False, comment="电子书价格")
    img = db.Column(db.String(250), nullable=False, comment="图书封面")

class Children(db.Model):

    __tablename__ = 'children'

    rank = db.Column(db.Integer, primary_key=True, comment="儿童读物排名")
    name = db.Column(db.String(100), nullable=False, comment="作者")
    bo_na = db.Column(db.String(100), nullable=False, comment="书名")
    url = db.Column(db.String(250), nullable=False, comment="图书地址")
    publishing = db.Column(db.String(30), nullable=False, comment="出版社")
    price = db.Column(db.String(30), nullable=False, comment="购买实价")
    ori_price = db.Column(db.String(30), nullable=False, comment="原价")
    ebook = db.Column(db.String(30), nullable=False, comment="电子书价格")
    img = db.Column(db.String(250), nullable=False, comment="图书封面")

class Natural_Sciences(db.Model):

    __tablename__ = 'natural_sciences'

    rank = db.Column(db.Integer, primary_key=True, comment="畅销榜排名")
    name = db.Column(db.String(100), nullable=False, comment="作者")
    bo_na = db.Column(db.String(100), nullable=False, comment="书名")
    url = db.Column(db.String(250), nullable=False, comment="图书地址")
    publishing = db.Column(db.String(30), nullable=False, comment="出版社")
    price = db.Column(db.String(30), nullable=False, comment="购买实价")
    ori_price = db.Column(db.String(30), nullable=False, comment="原价")
    ebook = db.Column(db.String(30), nullable=False, comment="电子书价格")
    img = db.Column(db.String(250), nullable=False, comment="图书封面")