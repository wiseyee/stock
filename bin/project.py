import tushare as ts
from conf.config import (database_setting as db_setting,
                         tushare_setting as ts_setting)
from data.init import init_all_tables
from data.update import DataUpdater


class Project():
    tools = {}

    # init the tools for project
    def __init__(self):
        self.tools['engine'] = init_all_tables(db_setting)
        self.tools['ts'] = ts.pro_api(ts_setting['token'])

    # run the schedule to process data in a specific cycle
    def run(self):
        updater = DataUpdater(engine=self.tools['engine'],
                              ts=self.tools['ts'])
        updater.update_every_working_day()
