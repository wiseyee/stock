import time
import pandas as pd
from data.db import engine, session
from data.api import tushare_pro as api
from data.model.update_record import UpdateRecord
from data.model.stock_company import StockCompany
from util.dater import Dater


class StockCompanyUpdater:
    """ stock_company 数据更新器 """

    def start(self):
        # 查看今日是否已经更新过
        update_record = session.query(UpdateRecord).filter(
            UpdateRecord.table == StockCompany.__tablename__).one()
        if update_record and update_record.last_updating == Dater.today():
            return

        # 获取：DB 数据 API 数据
        ts_data = api.stock_company()
        db_data = pd.read_sql_table('stock_company', engine)

        # 对比数据，排重
        if not db_data.empty:
            exists = db_data['ts_code']
            ta_data = ts_data[~ts_data['ts_code'].isin(exists)]
        else:
            ta_data = ts_data

        # 将需要更新的数据保存到数据库
        if not ta_data.empty:
            ta_data.to_sql('stock_company', engine,
                           if_exists='append', index=False)

        # 记录最近更新日期
        record = session.query(UpdateRecord).filter(
            UpdateRecord.table == StockCompany.__tablename__).one()
        record.last_updating = Dater.today()
        session.commit()
