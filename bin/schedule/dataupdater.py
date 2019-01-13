import tushare as ts

class DataUpdater():
    '''
    数据更新器
    1. 从 tushare 获取数据
    2. 将数据存入本地数据库
    '''
    ts = None

    def __init__(self, token):
        self.ts = ts.pro_api(token)

    def load_data_from_ts(self, func, **args):
        return self.ts.func(**args)