from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey
from data.db import ModelBase


class Concept(ModelBase):
    """ 股票概念分类 """
    __tablename__ = 'concept'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(8))    # 概念代码
    name = Column(Text)     # 概念名称
    src = Column(String(8))     # 概念来源