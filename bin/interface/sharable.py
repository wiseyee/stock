# 共享接口
class Sharable:
    __pool = {}

    def __init__(self):
        """ 实现共享 """
        pool_desc = ''.join(('_',self.__class__.__name__,'__pool'))
        if not pool_desc in dir(self):
            raise Warning('实现 Sharable 的对象必须默认带有属性 __pool')
        self.__dict__ = self.__pool
