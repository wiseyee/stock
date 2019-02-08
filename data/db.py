from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from conf.config import setting


CONN_DESC = "{type}+{connector}://{user}:{password}@{host}:{port}/{name}".format(**setting['db'])
engine = create_engine(CONN_DESC, encoding=setting['db']['encoding'], echo=setting['db']['debug'])
session = sessionmaker(bind=engine)()
ModelBase = declarative_base()
