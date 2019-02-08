from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey
from data.db import ModelBase


class TradeCalendar(ModelBase):
    """ 交易日历 """
    __tablename__ = 'trade_calendar'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cal_date = Column(String(8))        # 日历日期
    exchange = Column(String(4))        # 交易所
    is_open = Column(Integer)           # 是否开市
    is_weekly = Column(Integer)         # 是否为周最后一个交易日
    is_monthly = Column(Integer)        # 是否为月最后一个交易日
