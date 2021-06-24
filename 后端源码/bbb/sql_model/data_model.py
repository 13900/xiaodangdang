from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.Model):

    # 用户数库
    __tablename__ = 'user'
    email = db.Column(db.String(30), primary_key=True, nullable=False, comment="电子邮箱")
    password = db.Column(db.String(10), nullable=False, comment="密码")

