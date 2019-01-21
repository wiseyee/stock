from bin.interface.associated import Associated


# 项目框架，按流程调度各功能模块完成具体任务
class Project(Associated):

    def run(self):
        """ 项目对外运行接口 """
        self.__init()
        self.run_schedule()

    def __init(self):
        """ 项目初始化工作 """
        db = self.pivot.builder('Database')
        db.init_tables()  # 初始化数据库表

    def run_schedule(self):
        """ 按照指定计划运行 """
        scheduler = self.pivot.builder('Scheduler')
        print(scheduler)