import tushare as ts
from conf.config import database_setting as db_setting, tushare_setting as ts_setting
from bin.db.setup import init_all_tables


class Project():
    engine = None

    def __init__(self):
        self.engine = init_all_tables(db_setting)

    def load_data_from_ts(self, method, **args):
        pass

    def update_data_to_table(self, ts_data, table):
        pass

    def run(self):
        print('project running')
