from bin.implement.builder import Builder
from bin.implement.scheduler import Scheduler


# 项目框架，按流程调度各功能模块完成具体任务
class Project():

    def run(self):
        """ 项目对外运行接口 """
        self.__init()
        self.__run_schedule()

    def __init(self):
        """ 项目初始化工作 """
        Builder.build_db()

    def __run_schedule(self):
        """ 项目计划任务 """
        Scheduler.update_data()