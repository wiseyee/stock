from conf.config import database_setting as db_setting, tushare_setting as ts_setting
from bin.db.setup import init_all_tables
import tushare as ts


class Project():

    def __init__(self):
        init_all_tables(db_setting)

    def load_data_from_ts(self, method, **args):
        return ts.func(**args)

    def update_data_to_table(self, ts_data, table):
        # ts_data.to_sql(table, engine, if_exists='suspend')
        pass

    def run(self):
        print('project running')
