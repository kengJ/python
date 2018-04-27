# Flask 框架
安装:sudo pip install flask

数据层概念:
orm:对象关系映射
odm:对象文档映射
sql:用高效且紧凑的形式存储结构化数据
nosql:集合代替表，使用文档代替记录

处理配置文件
https://blog.csdn.net/shortwall/article/details/78615368
利用configparser包处理（python自带）
1.读取
import ConfigParser
cf=ConfigParser.ConfigParser()
cf.read(path) 读配置文件（ini、conf）返回结果是列表
cf.sections() 获取读到的所有sections(域)，返回列表类型
cf.options('sectionname') 某个域下的所有key，返回列表类型
cf.items('sectionname') 某个域下的所有key，value对
value=cf.get('sectionname','key') 获取某个yu下的key对应的value值
cf.type(value) 获取的value值的类型

1）getint(section, option)
获取section中option的值，返回int类型数据，所以该函数只能读取int类型的值。
2）getboolean(section, option)
获取section中option的值，返回布尔类型数据，所以该函数只能读取boolean类型的值。
3）getfloat(section, option)
获取section中option的值，返回浮点类型数据，所以该函数只能读取浮点类型的值。
4）has_option(section, option)
检测指定section下是否存在指定的option，如果存在返回True，否则返回False。
5）has_section(section)
检测配置文件中是否存在指定的section，如果存在返回True，否则返回False

2.写入
import configparser#加载现有配置文件
conf = configparser.ConfigParser()#写入配置文件
conf.add_section('config') #添加section
conf.set('config', 'v1', '100')#添加值
conf.set('config', 'v2', 'abc')#添加值
conf.set('config', 'v3', 'true')#添加值
conf.set('config', 'v4', '123.45')#添加值
with open('conf.ini', 'w') as fw:# 写入文件
    conf.write(fw)


数据层框架:
Flask-SQLAlchemy:flask 数据集成框架
安装:sudo pip install flask-sqlalchemy

Flask-SQLAlchemy链接数据库url:
MySQL mysql://username:password@hostname/database
Postgres postgresql://username:password@hostname/database
SQLite（ Unix） sqlite:////absolute/path/to/database
SQLite（ Windows） sqlite:///c:/absolute/path/to/database

配置:
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

