import threading
from bin.init import init_tables, init_data
from bin.update import Updater
from bin.forcast import Forecaster


# 项目框架
class Project():
    threads = set()

    # 项目对外运行接口
    def run(self):
        """ 初始化 """
        init_tables()
        init_data()
        """ 多线程运行项目各功能单元 """
        self.dipatch_thread()
        self.start_all_thread()

    def dipatch_thread(self):
        """ 给指定功能单元分配线程 """
        self.threads.add(threading.Thread(target=Updater().run, name='update'))
        self.threads.add(threading.Thread(target=Forecaster().run, name='forecast'))

    def start_all_thread(self):
        """ 启动所有线程 """
        for thread in self.threads:
            thread.start()
            thread.join()
