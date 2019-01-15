# 基础组件
class Util():
    utils = {}  # 公用组件池

    # 将单个组件放入组件池中
    # 值不能为 None，如果检测为 None 值，抛出异常
    # 返回添加后的整个组件池
    def add_util(self, name, util):
        if util is None:
            raise Exception('取值不能为 None')
        self.utils[name] = util
        return self.utils
    
    # 递归的方法将一组组件添加到组件池中
    # 值不能为 None
    # 返回添加后的整个组件池
    def add_utils(self, utils):
        for (k,v) in utils.items():
            self.add_util(k,v)
        return self.utils

    # 递归的方法从组件池中搜索键值为 key 的组件
    # 返回找到的组件
    # 没有匹配项返回 None
    def get_util(self, key, target = None):
        target = self.utils if target is None else target
        for (k,v) in target.items():
            if k == key:
                return v
            if isinstance(v,dict):
                return self.get_util(key, target = v)
        else:
            return None

    # 返回组件池中所有组件
    def get_utils(self):
        return self.utils

    # 组件池中键值为 key 的组件
    # 返回剩下的组件
    def remove_util(self, name):
        self.utils.pop(name, self.utils)
        return self.utils
