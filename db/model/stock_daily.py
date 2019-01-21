from db.model.base import Base
from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey


# 股票日线数据
class StockDaily(Base):
    __tablename__ = 'stock_daily'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9), nullable=False)  # ts 代码
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
