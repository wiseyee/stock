import time
from apscheduler.schedulers.blocking import BlockingScheduler
from data.updater.trade_calendar import TradeCalendarUpdater
from data.updater.stock_basic import StockBasicUpdater
from data.updater.stock_company import StockCompanyUpdater
from data.updater.stock_monthly import StockMonthlyUpdater
from data.updater.stock_weekly import StockWeeklyUpdater
from data.updater.stock_daily import StockDailyUpdater
from data.updater.daily_basic import DailyBasicUpdater
from data.updater.concept import ConceptUpdater
from data.updater.concept_detail import ConceptDetailUpdater
from util.logger import Logger
from util.loader import Loader


# 数据更新器
class Updater:
    jobs = {}
    updating = set()

    def run(self):
        """ 按计划更新数据 """
        sche = BlockingScheduler()
        sche._logger = Logger.get_logger()

        """ trade_calendar：每天，00:00 """
        self.jobs['update_trade_calendar'] = sche.add_job(
            self.__update_trade_calendar, 'cron', day='*')

        """ stock_basic ：每天，00:00 """
        self.jobs['update_stock_basic'] = sche.add_job(
            self.__update_stock_basic, 'cron', day='*')

        """ stock_company ：每天，00:00 """
        self.jobs['update_stock_company'] = sche.add_job(
            self.__update_stock_company, 'cron', day='*')

        """ daily_basic is running：工作日，17:30 """
        self.jobs['update_daily_basic'] = sche.add_job(
            self.__update_daily_basic, 'cron', day_of_week='mon-fri', hour='17', minute='30')

        """ stock_daily is running：工作日，17:30 """
        self.jobs['update_stock_daily'] = sche.add_job(
            self.__update_stock_daily, 'cron', day_of_week='mon-fri', hour='17', minute='30')

        """ stock_weekly is running：每周6，00:00 """
        self.jobs['update_stock_weekly'] = sche.add_job(
            self.__update_stock_weekly, 'cron', day_of_week='sat')

        """ stock_monthly is running：每月，第一天 """
        self.jobs['update_stock_monthly'] = sche.add_job(
            self.__update_stock_monthly, 'cron', month='*')

        """ concept is running：每天 """
        self.jobs['update_concept'] = sche.add_job(
            self.__update_concept, 'cron', day='*')

        """ concept_detail is running：每天，01:00 """
        self.jobs['update_concept_detail'] = sche.add_job(
            self.__update_concept_detail, 'cron', day='*', hour='1')

        """ 开启所有计划任务 """
        sche.start()

    def __update_trade_calendar(self):
        """ 更新 trade_calendar 表 """
        t0 = time.time()
        self.updating.add('trade_calendar')
        try:
            TradeCalendarUpdater().start()
        except Exception as e:
            Logger.error(e)
            return
        finally:
            self.updating.remove('trade_calendar')
        Logger.info('Updating of trade_calendar last {}'.format(time.time()-t0))

    def __update_stock_basic(self):
        """ 更新 stock_basic 表 """
        t0 = time.time()
        self.updating.add('stock_basic')
        try:
            StockBasicUpdater().start()
        except Exception as e:
            Logger.error(e)
            return
        finally:
            self.updating.remove('stock_basic')
        Logger.info('Updating of stock_basic last {}'.format(time.time()-t0))

    def __update_stock_company(self):
        """ 更新 stock_company 表 """
        t0 = time.time()
        self.updating.add('stock_company')
        try:
            StockCompanyUpdater().start()
        except Exception as e:
            Logger.error(e)
            return
        finally:
            self.updating.remove('stock_company')
        Logger.info('Updating of stock_company last {}'.format(time.time()-t0))

    def __update_daily_basic(self):
        """ 更新 daily_basic 表 """
        t0 = time.time()
        # 当交易日历处于更新状态时保持等待
        while 1:
            if 'trade_calendar' not in self.updating:
                break
        self.updating.add('daily_basic')
        try:
            DailyBasicUpdater().start()
        except Exception as e:
            Logger.error(e)
            return
        finally:
            self.updating.remove('daily_basic')
        Logger.info('Updating of daily_basic last {}'.format(time.time()-t0))

    def __update_stock_daily(self):
        """ 更新 stock_daily 表 """
        t0 = time.time()
        # 当交易日历处于更新状态时保持等待
        while 1:
            if 'trade_calendar' not in self.updating:
                break
        self.updating.add('stock_daily')
        try:
            StockDailyUpdater().start()
        except Exception as e:
            Logger.error(e)
            return
        finally:
            self.updating.remove('stock_daily')
        Logger.info('Updating of stock_daily last {}'.format(time.time()-t0))

    def __update_stock_weekly(self):
        """ 更新 stock_weekly 表 """
        t0 = time.time()
        # 当交易日历处于更新状态时保持等待
        while 1:
            if 'trade_calendar' not in self.updating:
                break
        self.updating.add('stock_weekly')
        try:
            StockWeeklyUpdater().start()
        except Exception as e:
            Logger.error(e)
            return
        finally:
            self.updating.remove('stock_weekly')
        Logger.info('Updating of stock_weekly last {}'.format(time.time()-t0))

    def __update_stock_monthly(self):
        """ 更新 stock_monthly 表 """
        t0 = time.time()
        # 当交易日历处于更新状态时保持等待
        while 1:
            if 'trade_calendar' not in self.updating:
                break
        self.updating.add('stock_monthly')
        try:
            StockMonthlyUpdater().start()
        except Exception as e:
            Logger.error(e)
            return
        finally:
            self.updating.remove('stock_monthly')
        Logger.info('Updating of stock_monthly last {}'.format(time.time()-t0))

    def __update_concept(self):
        """ 更新 concept 表 """
        t0 = time.time()
        self.updating.add('concept')
        try:
            ConceptUpdater().start()
        except Exception as e:
            Logger.error(e)
            return
        finally:
            self.updating.remove('concept')
        Logger.info('Updating of concept last {}'.format(time.time()-t0))

    def __update_concept_detail(self):
        """ 更新 concept_detail 表 """
        t0 = time.time()
        # 当概念列表处于更新状态时保持等待
        while 1:
            if 'concept' not in self.updating:
                break
        self.updating.add('concept_detail')
        try:
            ConceptDetailUpdater().start()
        except Exception as e:
            Logger.error(e)
        finally:
            self.updating.remove('concept_detail')
        Logger.info('Updating of concept_detail last {}'.format(time.time()-t0))
