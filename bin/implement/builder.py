from bin.pivot import Pivot


class Builder:

    @classmethod
    def build_db(self):
        """ 初始化数据库 """
        data_factory = Pivot.factory('Data')
        data_factory.init_db()

