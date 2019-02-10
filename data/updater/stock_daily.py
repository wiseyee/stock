import time
import pandas as pd
from sqlalchemy import and_
from data.db import engine, session
from data.api import tushare_pro as api
from data.model.stock_daily import StockDaily
from data.model.trade_calendar import TradeCalendar
from data.updater.wrapper import record_update
from util.logger import Logger
from util.dater import Dater


class StockDailyUpdater:
    """ stock_daily 数据更新器 """

    @record_update(model=StockDaily)
    def start(self):
        # 设置读取数据的开始、结束日期
        start_date = ''
        end_date = Dater.today()

        # 获取本地数据查看是否需要更新
        record = session.query(StockDaily).order_by(
            StockDaily.id.desc()).first()
        if record:
            start_date = Dater.offset(record.trade_date, 1)
            if start_date > end_date:
                return

        # 获取交易日历中开始到结束日期范围内的开市
        records = session.query(TradeCalendar).filter(and_(TradeCalendar.cal_date >= start_date,
                                                           TradeCalendar.cal_date <= end_date,
                                                           TradeCalendar.is_open == 1)).all()
        # 根据日期记录循环读取 api 数据，存入本地数据库
        for row in records:
            ta_data = self.__get_data(row.cal_date)
            if not ta_data.empty:
                ta_data.to_sql('stock_daily', engine,
                                if_exists='append', index=False)

    def __get_data(self, trade_date, i=0):
        """ 获得指定交易日的数据 """
        ts_data = pd.DataFrame()
        # 10 次请求不成功，记录警告
        if i > 10:
            Logger.warning(
                'Request of tushare api daily() interface has failed more than 10 times')
            return
        # 尝试请求 api ，并捕获异常
        try:
            ts_data = api.daily(trade_date=trade_date)
        except Exception:
            Logger.info(
                'Request of tushare api daily() interface timeout try after 60s')
            time.sleep(60)
            return self.__get_data(trade_date, i+1)
        # 返回 api 数据
        return ts_data
