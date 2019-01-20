# 数据库建造者：
# 不需要实例化多个对象，只提供 classmethod
class Database:
    @classmethod
    def test(cls):
        print('test test')