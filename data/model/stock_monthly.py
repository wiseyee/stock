from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey
from data.db import ModelBase


class StockMonthly(ModelBase):
    """ 股票月线行情 """
    __tablename__ = 'stock_monthly'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9))  # ts 代码
    trade_date = Column(String(8))  # 交易日期
    open = Column(Float)  # 开盘价
    high = Column(Float)  # 最高价
    low = Column(Float)  # 最低价
    close = Column(Float)  # 收盘价
    pre_close = Column(Float)  # 昨收价
    change = Column(Float)  # 涨跌额
    pct_chg = Column(Float)  # 涨跌幅
    vol = Column(Float)  # 成交量
    amount = Column(Float)  # 成交额
