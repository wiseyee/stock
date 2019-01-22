from apscheduler.schedulers.background import BackgroundScheduler
import pandas as pd

from bin.pivot import Pivot


# 计划任务
class Scheduler:
    sync = BackgroundScheduler()  # 后台任务
    data = Pivot.factory('Data')  # 数据工厂
    engine = data.db_engine  # 数据库引擎
    api = data.api  # 获取外部数据接口
    jobs = {}  # 任务列表
    updating = []  # 正在被更新列表

    @classmethod
    def update_data(cls):
        """ 运行数据更新任务 """
        """ stock_basic 工作日，下午五点半循环执行 """
        cls.jobs['update_stock_basic'] = cls.sync.add_job(
            cls.__update_stock_basic(cls), 'cron', day_of_week='mon-fri', hour='17', minute='30')

    def __update_stock_basic(self):
        """ 更新 stock_basic 表 """
        self.updating.append('stock_basic')  # 加入正在被更新表
        ts_data = self.api.stock_basic()  # tushare 数据
        db_data = pd.read_sql_table('stock_basic', self.engine)  # 本地数据

        if not db_data.empty:
            """ 排除数据库已存在数据 """
            ts_data = ts_data[~ts_data['ts_code'].isin(
                db_data['ts_code'].tolist())]
        if not ts_data.empty:
            """ 将数据保存到数据库 """
            ts_data.to_sql('stock_basic', self.engine,
                           if_exists='append', index=False)

        self.updating = [x != 'stock_basic' for x in self.updating]  # 移除正在被更新表
