import sys
sys.path.append('../..')
from init.config import database_setting as db

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey, create_engine

'''
定义所有数据库表
''' 
Base = declarative_base()

class StockBasic(Base):
    '''
    股票基础信息
    1.  ts_code (tushare 代码)
    2.  symbol (股票代码)
    3.  name (股票名称)
    4.  area (所在区域)
    5.  industry (所属行业)
    6.  market (市场类型)
    7.  list_date (上市日期)
    '''
    __tablename__ = 'stock_basic'

    id          = Column(Integer, primary_key = True, autoincrement = True)
    ts_code     = Column(String(9), nullable = False)
    symbol      = Column(String(6), nullable = False)
    name        = Column(String(8), nullable = False)
    area        = Column(String(3), nullable = False)
    industry    = Column(String(8), nullable = False)
    market      = Column(String(3), nullable = False)
    list_date   = Column(String(8), nullable = False)

class TradeCalendar(Base):
    '''
    交易日历
    1.  交易所
    2.  日期
    3.  是否交易
    '''
    __tablename__ = 'trade_calendar'

    id       = Column(Integer, primary_key = True, autoincrement = True)
    exchange = Column(String(4), nullable = False)
    cal_date = Column(String(8), nullable = False)
    is_open  = Column(Integer, nullable = False)

class StockCompany(Base):
    '''
    上市公司基本信息
    1.  交易所
    2.  日期
    3.  是否交易
    '''
    __tablename__ = 'stock_company'

    id          = Column(Integer, primary_key = True, autoincrement = True)
    ts_code     = Column(String(9), nullable = False)
    exchange    = Column(String(4), nullable = False)
    chairman    = Column(String(10))
    manager     = Column(String(10))
    secretary   = Column(String(10))
    reg_capital = Column(Float, nullable = False)
    setup_date  = Column(String(8),nullable = False)
    province    = Column(String(5),nullable = False)
    city        = Column(String(10), nullable = False)
    website     = Column(Text)
    email       = Column(Text)
    employees   = Column(Integer, nullable = False)

'''
根据 config 中的配置信息链接数据库创建表
'''
db_type = db['type']
db = db[db_type]
connector = 'pymysql'
user = db['user']
password = db['password']
host = db['host']
port = db['port']
db_name = db['db_name']
encoding = db['encoding']
db_desc = "{db_type}+{connector}://{user}:{password}@{host}:{port}/{db_name}".format(db_type = db_type, connector = connector, user = user, password = password, host = host, port = port, db_name = db_name)

engine = create_engine(db_desc, encoding = 'utf-8', echo = True)
Base.metadata.create_all(engine)