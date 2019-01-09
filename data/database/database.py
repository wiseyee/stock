import sys
sys.path.append('../..')
from init.config import database_settings

class BasicDatabase():
    '''
    数据库基础类,实现数据库连接主要参数的设置
    创建实例时,默认使用 config 中的数据库配置参数
    '''
    db_type  = ''
    port     = ''
    host     = ''
    user     = ''
    password = ''
    database = ''
    charset  = ''
    conn = None
    sql = ''

    # 构造函数,默认使用 config 配置信息,设置数据库连接参数
    def __init__(self, **args):
        self.db_type = self.__class__.__name__.lower()
        settings = database_settings[self.db_type]
        self.port     = settings['port']
        self.host     = settings['host']
        self.user     = settings['user']
        self.password = settings['password']
        self.database = settings['database']
        self.charset  = settings['charset']
        self.set(**args)

    # 手动设置数据库连接参数,覆盖默认的 config 配置信息
    def set(self, **args):
        if 'port' in args.keys() :
            self.port = args['port']
        if 'host' in args.keys() :
            self.host = args['host']
        if 'user' in args.keys() :
            self.user = args['user']
        if 'password' in args.keys() :
            self.password = args['password']
        if 'database' in args.keys() :
            self.database = args['database']
        if 'charset' in args.keys() :
            self.charset = args['charset']

    # 规定数据库执行 sql 的通用方法, 子类定义具体实现
    def exec(self, sql):
        self.sql = sql;