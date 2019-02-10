import logging
import time
import os
from conf.config import setting


class Logger():
    """ 日志记录器 """
    
    # 记录级别列表
    levels = {'DEBUG': logging.DEBUG,
              'INFO': logging.INFO,
              'WARNING': logging.WARNING,
              'ERROR': logging.ERROR,
              'CRITICAL': logging.CRITICAL}
    # 配置文件设置的记录级别
    level = levels[setting['log']['level']]
    # 日志格式
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    # 控制台 handler
    console_handler = logging.StreamHandler(os.sys.stdout)
    # log 文件存放路径
    path = setting['log']['path']
    # logger 实例对象
    logger = None

    def __config_logger(self):
        """ 根据 config 配置 logger """
        self.logger.setLevel(self.level)
        filename = time.strftime('%Y-%m-%d', time.localtime()) + '.log'
        filepath = os.path.join(self.path, filename)
        file_handler = logging.FileHandler(filepath)
        file_handler.setFormatter(self.fmt)
        self.logger.addHandler(file_handler)
        # 根据配置文件选择是否要输出到控制台
        if setting['log']['show_in_console']:
            self.console_handler.setFormatter(self.fmt)
            self.logger.addHandler(self.console_handler)

    @classmethod
    def get_logger(cls):
        """ 取得 logger 实例 """
        if cls.logger is None:
            cls.logger = logging.getLogger('mylogger')
            cls.__config_logger(cls)
        return cls.logger

    @classmethod
    def debug(cls, msg):
        """ 包装 debug 类方法 """
        cls.get_logger().debug(msg)

    @classmethod
    def info(cls, msg):
        """ 包装 info 类方法 """
        cls.get_logger().info(msg)

    @classmethod
    def warning(cls, msg):
        """ 包装 warning 类方法 """
        cls.get_logger().warning(msg)

    @classmethod
    def error(cls, msg):
        """ 包装 error 类方法 """
        cls.get_logger().error(msg)

    @classmethod
    def critical(cls, msg):
        """ 包装 critical 类方法 """
        cls.get_logger().critical(msg)
