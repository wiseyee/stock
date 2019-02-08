from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey
from data.db import ModelBase


class StockBasic(ModelBase):
    """ 股票基础信息 """
    __tablename__ = 'stock_basic'
    
    id = Column(Integer, primary_key=True)
    ts_code = Column(String(9))  # ts 股票代码
    symbol = Column(String(6))  # 股票代码
    name = Column(String(8))  # 股票名称
    area = Column(String(3))  # 所在区域
    industry = Column(String(8))  # 所属行业
    market = Column(String(3))  # 市场类型
    list_date = Column(String(8))  # 上市日期
