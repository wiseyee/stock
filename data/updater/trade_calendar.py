import time
import pandas as pd
from data.db import engine, session
from data.api import tushare_pro as api
from data.model.trade_calendar import TradeCalendar
from data.model.update_record import UpdateRecord
from util.logger import Logger
from util.dater import Dater


class TradeCalendarUpdater:
    """ trade_calendar 数据更新器 """

    def start(self):
        """ 更新 trade_calendar 表 """
        # 查看今日是否已经更新过
        update_record = session.query(UpdateRecord).filter(
            UpdateRecord.table == TradeCalendar.__tablename__).one()
        if update_record and update_record.last_updating == Dater.today():
            return

        # 设置读取数据的开始、结束日期
        start_date = ''
        end_date = Dater.month_end()

        # 获取本地数据查看数据是否需要更新
        record = session.query(TradeCalendar).order_by(
            TradeCalendar.id.desc()).first()
        if record:
            start_date = Dater.offset(record.cal_date, 1)
            if start_date > end_date:
                return

        # 对比最新日期和目标日期，继续补足目标数据
        ta_data = pd.DataFrame()
        while start_date < Dater.offset(end_date, 7):
            ts_data = self.__get_data(start_date, Dater.offset(end_date, 7))
            if not ts_data.empty:
                ta_data = pd.concat([ta_data, ts_data], ignore_index=True)
            latest_date = ta_data['cal_date'].iloc[-1]
            start_date = Dater.offset(latest_date, 1)
            pass

        # 将还需更新的数据存入数据库
        if not ta_data.empty:
            ta_data = self.update_weekly_monthly(ta_data, end_date)
            ta_data.to_sql('trade_calendar', engine,
                           if_exists='append', index=False)

        # 记录最近更新日期
        record = session.query(UpdateRecord).filter(
            UpdateRecord.table == TradeCalendar.__tablename__).one()
        record.last_updating = Dater.today()
        session.commit()

    def __get_data(self, start, end, i=0):
        """ 获得指定日期的数据 """
        ts_data = pd.DataFrame()
        # 10 次请求不成功，记录警告
        if i > 10:
            Logger.warning(
                'Request of tushare api trade_cal() interface has failed more than 10 times')
            return
        # 尝试请求 api，并捕获异常
        try:
            ts_data = api.trade_cal(start_date=start, end_date=end)
        except Exception:
            Logger.info(
                'Request of tushare api trade_cal() interface timeout try after 60s')
            time.sleep(60)
            return self.__get_data(start, end, i+1)
        # 返回 api 数据
        return ts_data

    def update_weekly_monthly(self, df, end):
        """ 为周最后一个交易日，月最后一个交易日添加标识 """
        calendar = df.copy()
        # 未开市日期的 dataframe
        dates1 = calendar[calendar['is_open'] == 0].copy()
        dates1['is_weekly'] = 0
        dates1['is_monthly'] = 0
        dates1 = dates1[['cal_date', 'is_weekly', 'is_monthly']]
        # 开市日期的 dataframe
        dates2 = calendar[calendar['is_open'] == 1].copy()
        dates2['next_date'] = dates2['cal_date'].shift(-1)
        dates2['is_weekly'] = dates2.apply(
            lambda row: 0 if Dater.isin_same_week(row['cal_date'], row['next_date']) else 1, axis=1)
        dates2['is_monthly'] = dates2.apply(
            lambda row: 0 if Dater.isin_same_month(row['cal_date'], row['next_date']) else 1, axis=1)
        dates2 = dates2[['cal_date', 'is_weekly', 'is_monthly']]
        # 合并所有日期生成完整标识 dataframe
        labels = dates1.append(dates2)
        # 排除掉日历中原来的标识 columns
        calendar = calendar[['cal_date', 'exchange', 'is_open']]
        # 合并生成带标识的 dataframe 并返回结果
        calendar = calendar.merge(labels, on='cal_date', how='outer')
        calendar = calendar[calendar['cal_date'] <= end]
        return calendar
