from db.model.base import Base
from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey


# 交易日历
class TradeCalendar(Base):
    __tablename__ = 'trade_calendar'

    id = Column(Integer, primary_key=True, autoincrement=True)
    exchange = Column(String(4))  # 交易所
    cal_date = Column(String(8))  # 日历日期
    is_open = Column(Integer)  # 是否交易
