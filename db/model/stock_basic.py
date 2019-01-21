from db.model.base import Base
from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey


# 股票基础信息
class StockBasic(Base):
    __tablename__ = 'stock_basic'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9), nullable=False)  # ts 股票代码
    symbol = Column(String(6))  # 股票代码
    name = Column(String(8))  # 股票名称
    area = Column(String(3))  # 所在区域
    industry = Column(String(8))  # 所属行业
    market = Column(String(3))  # 市场类型
    list_date = Column(String(8))  # 上市日期
