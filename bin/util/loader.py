# 类加载器
class Loader():

    @classmethod
    def load(cls, path, target):
        """ 通过 path 加载指定类 """
        module = __import__(path, fromlist=(target))
        return eval('module.' + target)
