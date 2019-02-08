import time
import pandas as pd
from data.db import engine
from data.api import tushare_pro as api


class StockBasicUpdater:
    """ stock_basic 数据更新器 """

    def start(self):
        # 获取：DB 数据 API 数据
        ts_data = api.stock_basic()
        db_data = pd.read_sql_table('stock_basic', engine)

        # 对比数据，排重
        if not db_data.empty:
            exists = db_data['ts_code']
            ta_data = ts_data[~ts_data['ts_code'].isin(exists)]
        else:
            ta_data = ts_data

        # 将需要更新的数据保存到数据库
        if not ta_data.empty:
            ta_data.to_sql('stock_basic', engine,
                           if_exists='append', index=False)