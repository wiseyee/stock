from bin.util import Util
from data.builder import DataBuilder
from data.updater import DataUpdater


class Project(Util):
    # 初始化项目组件
    def __init__(self):
        data_builder = DataBuilder()  # 实例化 DataBuilder
        data_builder.build_tables()   # 创建数据库表

    # 运行主进程
    def run(self):
        data_updater = DataUpdater()  # 实例化 DataUpdater
        print(self.utils)
