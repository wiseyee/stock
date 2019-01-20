from bin.interface.associated import Associated


# 项目框架，按流程调度各功能模块完成具体任务
class Project(Associated):
    def run(self):
        """ 项目对外运行接口 """
        db = self.pivot.builder('Database')
        db.test()
