from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ip_database(db.Model):


    __tablename__ = 'ip_database'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(30), nullable=False, comment="IP地址")
    types = db.Column(db.String(30), nullable=False, comment="IP类型")
    location = db.Column(db.String(30), nullable=False, comment="IP所在地")
