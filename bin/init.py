from data.db import ModelBase, engine
from util.loader import Loader
from util.logger import Logger
from data.updater.trade_calendar import TradeCalendarUpdater
from data.updater.stock_basic import StockBasicUpdater
from data.updater.stock_company import StockCompanyUpdater
from data.updater.stock_monthly import StockMonthlyUpdater
from data.updater.stock_weekly import StockWeeklyUpdater
from data.updater.stock_daily import StockDailyUpdater
from data.updater.daily_basic import DailyBasicUpdater
from data.updater.concept import ConceptUpdater
from data.updater.concept_detail import ConceptDetailUpdater


def init_tables():
    """ 初始化数据库表 """
    Loader.load_class_from_dir('data/model')
    ModelBase.metadata.create_all(engine)
    Logger.info('Initialization of the tables has been completed')


def init_data():
    """ 初始化数据 """
    print('Initialization of the data will take a long time please wait')
    TradeCalendarUpdater().start()
    Logger.info('trade_calendar data has been initialized')
    StockBasicUpdater().start()
    Logger.info('stock_basic data has been initialized')
    StockCompanyUpdater().start()
    Logger.info('stock_company data has been initialized')
    StockMonthlyUpdater().start()
    Logger.info('stock_monthly data has been initialized')
    StockWeeklyUpdater().start()
    Logger.info('stock_weekly data has been initialized')
    StockDailyUpdater().start()
    Logger.info('stock_daily data has been initialized')
    DailyBasicUpdater().start()
    Logger.info('daily_basic data has been initialized')
    ConceptUpdater().start()
    Logger.info('concept data has been initialized')
    ConceptDetailUpdater().start()
    Logger.info('concept_detail data has been initialized')
    Logger.info('All initialization of data has been completed')
