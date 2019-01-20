from bin.interface.sharable import Sharable
from bin.interface.associated import Associated


# 仓库
class Repo(Sharable, Associated):
    __pool = {}  # 存储池

    def update(self, *args, **kargs):
        """ 更新要存储的对象到仓库存储池 """
        for arg in args:
            if isinstance(arg, dict):
                self.update(**arg)
            else:
                raise Exception('参数 {arg} 必须为字典或关键字参数')
        self.__pool = dict(self.__pool, **kargs)

    def get(self, key):
        """ 取得仓库中的对象 """
        return self.__pool[key] if key in self.__pool else None

    def pop(self, key):
        """ 取出并删除仓库中的对象 """
        return self.__pool.pop(key, None)

    def remove(self, key):
        """ 通过 key 删除仓库已存储对象 """
        if key in self.__pool:
            self.__pool.pop(key)
        else:
            raise Warning('仓库中不存在 {key}'.format(key=key))

    def show(self):
        """ 展示仓库已存储对象 """
        print(self.__pool)

    def __getattr__(self, key):
        """ 访问仓库自身不存在属性时，在仓库存储池中寻找符合条件对象 """
        return self.get(key)
