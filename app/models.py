from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://movieuser:movie@127.0.0.1/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# 注册会员
class = UserRegister(db.Model):
    __tablename__ = "userregister"
    id = db.Column(db.Integer,primary_key=True) # 编号
    name = db.Column(db.String(100), unique=True) # 昵称
    pwd = db.Column(db.String(100), unique=True) # 密码
    email = db.Column(db.String(100), unique=True) # 邮箱
    phone = db.Column(db.String(11), unique=True) # 手机号码
    info = db.Column(db.Text) # 个性简介
    face = db.Column(db.String(255), unique=True) # 头像
    regtime = db.Column(db.DateTime, index=True, default=datetime.utcnow) # 注册时间
    uuid = db.Column(db.String(255), unique=True) # 唯一标识符
    userloginlog = db.relationship('UserLoginLog', backref='userregister') # 会员日志外键关系

def __repr__(self):
    return "<User %r>" % self.name

# 会员登录日志
class UserLoginLog(db.MOdel):
    __tablename__ = "userloginlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('userregister.id'))
    ip = db.Column(db.String(100), )
    logintime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<UserLoginLog %r>" % self.id