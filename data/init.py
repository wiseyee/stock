from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey, create_engine

Base = declarative_base()


def init_all_tables(db):
    """ 
    创建所有数据库表
    """
    db_type = db['type']
    db = db[db_type]
    connector = 'pymysql'
    user = db['user']
    password = db['password']
    host = db['host']
    port = db['port']
    db_name = db['db_name']
    encoding = db['encoding']
    db_desc = "{db_type}+{connector}://{user}:{password}@{host}:{port}/{db_name}".format(db_type=db_type,
                                                                                         connector=connector,
                                                                                         user=user,
                                                                                         password=password,
                                                                                         host=host,
                                                                                         port=port,
                                                                                         db_name=db_name)

    engine = create_engine(db_desc, encoding=encoding, echo=True)
    Base.metadata.create_all(engine)

    return engine


class StockBasic(Base):
    """
    股票基础信息
    1.  ts_code (tushare 代码)
    2.  symbol (股票代码)
    3.  name (股票名称)
    4.  area (所在区域)
    5.  industry (所属行业)
    6.  market (市场类型)
    7.  list_date (上市日期)
    """
    __tablename__ = 'stock_basic'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9), nullable=False)
    symbol = Column(String(6), nullable=False)
    name = Column(String(8), nullable=False)
    area = Column(String(3), nullable=False)
    industry = Column(String(8), nullable=False)
    market = Column(String(3), nullable=False)
    list_date = Column(String(8), nullable=False)


class TradeCalendar(Base):
    """
    交易日历
    1.  exchange (交易所)
    2.  cal_date (日历日期)
    3.  is_open (是否交易)
    """
    __tablename__ = 'trade_calendar'

    id = Column(Integer, primary_key=True, autoincrement=True)
    exchange = Column(String(4), nullable=False)
    cal_date = Column(String(8), nullable=False)
    is_open = Column(Integer, nullable=False)


class StockCompany(Base):
    """
    上市公司基本信息
    1.  ts_code (tushare 代码)
    2.  exchange (交易所)
    3.  chairman (法人代表)
    4.  manager (总经理)
    5.  secretary (董秘)
    6.  reg_capital (注册资本)
    7.  setup_date (注册日期)
    8.  province (所在省份)
    9.  city (所在城市)
    10. website (公司网站)
    11. email (电子邮件)
    12. employees (员工人数)
    """
    __tablename__ = 'stock_company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9), nullable=False)
    exchange = Column(String(4), nullable=False)
    chairman = Column(String(10))
    manager = Column(String(10))
    secretary = Column(String(10))
    reg_capital = Column(Float, nullable=False)
    setup_date = Column(String(8), nullable=False)
    province = Column(String(5), nullable=False)
    city = Column(String(10), nullable=False)
    website = Column(Text)
    email = Column(Text)
    employees = Column(Integer, nullable=False)


class StockDaily(Base):
    """
    股票日线数据
    1.  ts_code (tushare 代码)
    2.  trade_date (交易日期)
    3.  open (开盘价)
    4.  high (最高价)
    5.  low (最低价)
    6.  close (收盘价)
    7.  pre_close (昨收价)
    8.  change (涨跌额)
    9.  pct_chg (涨跌幅)
    10. vol (成交量)
    11. amount (成交额)
    """
    __tablename__ = 'stock_daily'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9), nullable=False)
    trade_date = Column(String(8), nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    pre_close = Column(Float, nullable=False)
    change = Column(Float, nullable=False)
    pct_chg = Column(Float, nullable=False)
    vol = Column(Float, nullable=False)
    amount = Column(Float, nullable=False)
