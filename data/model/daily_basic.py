from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey
from data.db import ModelBase


class DailyBasic(ModelBase):
    """ 股票每日指标 """
    __tablename__ = 'daily_basic'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9))  # ts 代码
    trade_date = Column(String(8))  # 交易日期
    close = Column(Float)  # 收盘价
    turnover_rate = Column(Float)  # 换手率
    turnover_rate_f = Column(Float)  # 流通盘换手率
    volume_ratio = Column(Float)  # 量比
    pe = Column(Float)  # 市盈率
    pe_ttm = Column(Float)  # 滚动市盈率
    pb = Column(Float)  # 市净率
    ps = Column(Float)  # 市销率
    ps_ttm = Column(Float)  # 动态市销率
    total_share = Column(Float)  # 总股本(万)
    float_share = Column(Float)  # 流通股本(万)
    free_share = Column(Float)  # 自由流通股本(万)
    total_mv = Column(Float)  # 总市值(万元)
    circ_mv = Column(Float)  # 流通市值(万元)
