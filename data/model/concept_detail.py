from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey
from data.db import ModelBase


class ConceptDetail(ModelBase):
    """ 股票概念明细 """
    __tablename__ = 'concept_detail'

    id = Column(Integer, primary_key=True)
    code = Column(String(8))      # 概念代码
    ts_code = Column(String(9))    # ts 代码
    name = Column(String(8), nullable=False)     # 股票名称