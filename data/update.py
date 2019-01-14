from apscheduler.schedulers.background import BackgroundScheduler


class DataUpdater():
    engine = None
    ts = None
    jobs = {}

    def __init__(self, engine, ts):
        self.engine = engine
        self.ts = ts

    # 执行所有更新操作
    def update_every_working_day(self):
        scheduler = BackgroundScheduler()
        self.jobs['stock_basic'] = scheduler.add_job(
            self.update_stock_basic, 'cron', day_of_week='0-4', hour=17)
        self.jobs['trade_calendar'] = scheduler.add_job(
            self.update_trade_calendar, 'cron', day_of_week='0-4', hour=17)
        self.jobs['stock_company'] = scheduler.add_job(
            self.update_stock_company, 'cron', day_of_week='0-4', hour=17)
        self.jobs['stock_daily'] = scheduler.add_job(
            self.update_stock_daily, 'cron', day_of_week='0-4', hour=17)
        scheduler.start()
        # scheduler.print_jobs()

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
