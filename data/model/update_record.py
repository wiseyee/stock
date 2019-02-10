from sqlalchemy import Column, Text, String, Integer, Float, ForeignKey
from data.db import ModelBase


class UpdateRecord(ModelBase):
    __tablename__ = 'update_record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    table = Column(String(20), nullable=False)     # 表名称
    last_updating = Column(String(8), nullable=False)       # 最近更新日期