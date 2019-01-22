# 共享接口
class Sharable:
    __pool = {}

    def __init__(self):
        """ 实现共享 """
        self.__dict__ = self.__pool
