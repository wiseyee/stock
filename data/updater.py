from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import tushare as ts

from bin.util import Util
from conf.config import tushare_setting as ts_setting


# 数据更新操作器
class DataUpdater(Util):

    def __init__(self):
        self.asyn_scheduler = BackgroundScheduler()  # 非阻塞式调度器
        self.sync_scheduler = BlockingScheduler()    # 阻塞式调度器
        self.engine = self.get_util('engine')        # 数据库引擎
        self.session = self.get_util('session')      # 数据库会话
        ts.set_token(ts_setting['token'])
        self.ts = ts                                 # tushare.org API
        self.pro = ts.pro_api()                      # tushare.pro API
        # 数据库表已更新标示，用于控制非阻塞式任务的先后顺序
        self.flags = {'stock_basic_updated': False,
                      'trade_calendar_updated': False,
                      'stock_company_updated': False,
                      'stock_daily_updated': False,
                      'stock_weekly_updated': False,
                      'stock_monthly_updated': False}

    # 更新 stock_basic 表
    def update_stock_basic(self):
        stock_basic = self.pro.stock_basic()
        stock_basic.to_sql('stock_basic', self.engine, if_exists = 'append')
        self.flags['stock_basic_updated'] = True

    # 更新 trade_calendar 表
    def update_trade_calendar(self):
        trade_canlendar = self.pro.trade_calendar()
        
    # 更新 stock_company 表
    def update_stock_company(self):
        print('update stock company')

    # 更新 stock_daily 表
    def update_stock_daily(self):
        print('update stock daily')

    # 重置更新状态标志
    def reset_flags(self):
        for k in self.flags:
            self.flags[k] = False

    # 查看是否所有表全部更新完毕
    def if_all_updated(self):
        for flag in self.flags.values():
            if not flag:
                return False
        return True
