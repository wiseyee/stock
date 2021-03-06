import time
import pandas as pd
from sqlalchemy import and_
from data.db import engine, session
from data.api import tushare_pro as api
from data.model.stock_monthly import StockMonthly
from data.model.trade_calendar import TradeCalendar
from data.updater.wrapper import record_update
from util.logger import Logger
from util.dater import Dater


class StockMonthlyUpdater:
    """ stock_monthly 数据更新器 """

    @record_update(model=StockMonthly)
    def start(self):
        # 设置读取数据的开始、结束日期
        start_date = ''
        end_date = Dater.today()

        # 获取本地数据查看是否需要更新
        record = session.query(StockMonthly).order_by(
            StockMonthly.id.desc()).first()
        if record:
            start_date = Dater.offset(record.trade_date, 1)
            if start_date > end_date:
                return

        # 获取交易日历中开始到结束日期范围内的开市日期
        records = session.query(TradeCalendar).filter(and_(TradeCalendar.cal_date >= start_date,
                                                           TradeCalendar.cal_date <= end_date,
                                                           TradeCalendar.is_monthly == 1)).all()
        # 根据日历记录循环取得 api 数据，存入本地数据库
        for row in records:
            ta_data = self.__get_data(row.cal_date)
            if not ta_data.empty:
                ta_data.to_sql('stock_monthly', engine,
                                if_exists='append', index=False)

    def __get_data(self, trade_date, i=0):
        """ 获得指定交易日的数据 """
        ts_data = pd.DataFrame()
        # 10 次请求不成功，记录警告
        if i > 10:
            Logger.warning(
                'Request of tushare api monthly() interface has failed more than 10 times')
            return
        # 尝试请求 api ，并捕获异常
        try:
            ts_data = api.monthly(trade_date=trade_date)
        except Exception:
            Logger.info(
                'Request of tushare api monthly() interface timeout try after 60s')
            time.sleep(60)
            return self.__get_data(trade_date, i+1)
        # 返回 api 数据
        return ts_data
