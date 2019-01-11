from conf.config import database_setting as db_setting, tushare_setting as ts_setting
from bin.db.setup import init_all_tables

class Project():
    def __init__(self):
        self.session = init_all_tables(db_setting)

    def update_data(self):
        print(ts_setting)

    def run(self):
        self.update_data();

        