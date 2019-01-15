from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
import tushare as ts

from bin.util import Util
from conf.config import (database_setting as db_setting,
                         tushare_setting as ts_setting)


# 数据构造器
# 构造数据库表
# 实例化数据库操作常用组件存入组件池
class DataBuilder(Util):
    # 根据 config 配置信息生成数据库常用组件
    def __init__(self):
        self.db_type = db_setting['type']
        self.db_connector = db_setting['connector']
        self.db = db_setting[self.db_type]
        self.db_desc = "{type}+{connector}://{user}:{password}@{host}:{port}/{name}".format(type=self.db_type,
                                                                                            connector=self.db_connector,
                                                                                            user=self.db['user'],
                                                                                            password=self.db['password'],
                                                                                            host=self.db['host'],
                                                                                            port=self.db['port'],
                                                                                            name=self.db['name'])
        engine = create_engine(self.db_desc,
                               encoding=self.db['encoding'],
                               echo=self.db['debug'])           # SQLAlchemy engine
        session = sessionmaker(bind=engine)                     # SQLAlchemy session

        # 将 engine session 添加进组件池
        self.add_utils({'engine':engine, 'session':session})

    # 创建所有 ORM 数据库表
    def build_tables(self):  
        Base.metadata.create_all(self.get_util('engine'))


Base = declarative_base()


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
    symbol = Column(String(6))
    name = Column(String(8))
    area = Column(String(3))
    industry = Column(String(8))
    market = Column(String(3))
    list_date = Column(String(8))


class TradeCalendar(Base):
    """
    交易日历
    1.  exchange (交易所)
    2.  cal_date (日历日期)
    3.  is_open (是否交易)
    """
    __tablename__ = 'trade_calendar'

    id = Column(Integer, primary_key=True, autoincrement=True)
    exchange = Column(String(4))
    cal_date = Column(String(8))
    is_open = Column(Integer)


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
    exchange = Column(String(4))
    chairman = Column(String(10))
    manager = Column(String(10))
    secretary = Column(String(10))
    reg_capital = Column(Float)
    setup_date = Column(String(8))
    province = Column(String(5))
    city = Column(String(10))
    website = Column(Text)
    email = Column(Text)
    employees = Column(Integer)


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
    trade_date = Column(String(8))
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    pre_close = Column(Float)
    change = Column(Float)
    pct_chg = Column(Float)
    vol = Column(Float)
    amount = Column(Float)


class StockWeekly(Base):
    """ 
    股票周线行情
    1.  ts_code tushare 代码
    2.  trade_date 交易日期
    3.  close 收盘价
    4.  open 开盘价
    5.  high 最高价
    6.  low 最低价
    7.  pre_close 昨收盘价
    8.  change 涨跌额
    9.  pct_chg 涨跌幅
    10. vol 成交量
    11. amount 成交额
    """
    __tablename__ = 'stock_weekly'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9), nullable=False)
    close = Column(Float)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    pre_close = Column(Float)
    change = Column(Float)
    pct_chg = Column(Float)
    vol = Column(Float)
    amount = Column(Float)


class StockMonthly(Base):
    """ 
    股票月线行情
    1.  ts_code tushare 代码
    2.  trade_date 交易日期
    3.  close 收盘价
    4.  open 开盘价
    5.  high 最高价
    6.  low 最低价
    7.  pre_close 昨收盘价
    8.  change 月涨跌额
    9.  pct_chg 月涨跌幅
    10. vol 月成交量
    11. amount 月成交额
    """
    __tablename__ = 'stock_monthly'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9), nullable=False)
    trade_date = Column(String(8))
    close = Column(Float)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    pre_close = Column(Float)
    change = Column(Float)
    pct_chg = Column(Float)
    vol = Column(Float)
    amount = Column(Float)


class DailyBasic(Base):
    """ 
    股票每日指标
    1.  ts_code tushare 代码
    2.  trade_date 交易日期
    3.  close 收盘价
    4.  turnover_rate 换手率 %
    5.  turnover_rate_f 流通盘换手率 %
    6.  volume_ratio 量比
    7.  pe 市盈率
    8.  pe_ttm 动态市盈率
    9.  pb 市净率
    10. ps 市销率
    11. ps_ttm 动态市销率
    12. total_share 总股本(万)
    13. float_sahre 流通股本(万)
    14. free_share 自由流通股本(万)
    15. total_mv 总市值(万元)
    16. circ_mv 流通市值(万元)
    """
    __tablename__ = 'daily_basic'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9), nullable=False)
    trade_date = Column(String(8))
    close = Column(Float)
    turnover_rate = Column(Float)
    turnover_rate_f = Column(Float)
    volume_ratio = Column(Float)
    pe = Column(Float)
    pe_ttm = Column(Float)
    pb = Column(Float)
    ps = Column(Float)
    ps_ttm = Column(Float)
    total_share = Column(Float)
    float_sahre = Column(Float)
    free_share = Column(Float)
    total_mv = Column(Float)
    circ_mv = Column(Float)
