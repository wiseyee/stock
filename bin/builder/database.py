from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bin.interface.associated import Associated
from db.model.base import Base
from conf.config import setting


# 数据库建造者
class Database(Associated):
    db_setting = setting['db']
    conn_desc = "{type}+{connector}://{user}:{password}@{host}:{port}/{name}".format(
        **db_setting)
    engine = create_engine(
        conn_desc, encoding=db_setting['encoding'], echo=db_setting['debug'])
    session = sessionmaker(bind=engine)()
    model = {}

    @classmethod
    def init_tables(cls):
        """ 初始化数据库表 """
        cls.__load_models(cls)
        cls.model['Base'].metadata.create_all(cls.engine)

    def __load_models(self):
        """ 加载数据库表 model 类 """
        parser = self.pivot.util('Parser')
        loader = self.pivot.util('Loader')
        model_import_path = parser.parse_file_for_import('./db/model')
        for (k, v) in model_import_path.items():
            self.model[k] = loader.load(v,k)
