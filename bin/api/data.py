from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import tushare as ts

from bin.pivot import Pivot
from db.model.base import Base
from conf.config import setting
from bin.interface.sharable import Sharable


# 数据工厂
class Data():
    """ 数据库 """
    db_setting = setting['db']
    conn_desc = "{type}+{connector}://{user}:{password}@{host}:{port}/{name}".format(
        **db_setting)
    db_engine = create_engine(
        conn_desc, encoding=db_setting['encoding'], echo=db_setting['debug'])
    db_session = sessionmaker(bind=db_engine)()
    db_model = {}
    """ API """
    ts_setting = setting['tushare']
    api = ts.pro_api(ts_setting['token'])

    @classmethod
    def init_db(cls):
        """ 初始化数据库表 """
        cls.__load_models(cls)
        cls.db_model['Base'].metadata.create_all(cls.db_engine)

    def __load_models(self):
        """ 加载数据库表 model 类 """
        parser = Pivot.util('Parser')
        loader = Pivot.util('Loader')
        model_import_path = parser.parse_file_for_import('./db/model')
        for (k, v) in model_import_path.items():
            model = loader.load(v, k)
            self.db_model[k] = model

    @classmethod
    def set_api(cls, api):
        """ 设置获取数据的 API """
        cls.api = api
