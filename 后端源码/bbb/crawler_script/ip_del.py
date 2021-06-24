
from sql_model import ip_model

class Delete_Ip():
    db = ip_model.db
    @classmethod
    def del_ip(cls,app, ip):
        cls.db.init_app(app)
        if  ip != '' or ip != None:
            ip_dat = ip_model.ip_database
            rem = ip_dat.query.filter(ip_dat.address==ip).first()
            cls.db.session.delete(rem)
            cls.db.session.commit()
            print(id,'已删除')
        return 'ip删除结束'



