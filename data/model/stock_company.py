from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey
from data.db import ModelBase


class StockCompany(ModelBase):
    """ 上市公司基本信息 """
    __tablename__ = 'stock_company'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ts_code = Column(String(9))  # ts 代码
    exchange = Column(String(4))  # 交易所
    chairman = Column(Text)  # 法人代表
    manager = Column(Text)  # 总经理
    secretary = Column(Text)  # 董秘
    reg_capital = Column(Float)  # 注册资本
    setup_date = Column(String(8))  # 注册日期
    province = Column(String(5))  # 所在省份
    city = Column(String(10))  # 所在城市
    website = Column(Text)  # 公司网站
    email = Column(Text)  # 电子邮件
    employees = Column(Integer)  # 员工人数
