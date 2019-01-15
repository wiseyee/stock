from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

from bin.util import Util


# 数据更新操作器
class DataUpdater(Util):

    def __init__(self):
        # 将 BackgroundScheduler BlockingScheduler 添加进组件池
        self.add_utils({'background_scheduler':BackgroundScheduler(),
                        'blocking_scheduler':BlockingScheduler()})


    # 后台并发线程更新
    def update_in_background_schedule(self):
        pass

    # 主线程阻塞式更新
    def update_in_blocking_schedule(self):
        pass

    # 更新 stock_basic 表
    def update_stock_basic(self):
        print('update stock basic')

    # 更新 trade_calendar 表
    def update_trade_calendar(self):
        print('update trade calendar')
    # 更新 stock_company 表

    def update_stock_company(self):
        print('update stock company')

    # 更新 stock_daily 表
    def update_stock_daily(self):
        print('update stock daily')
