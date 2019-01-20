from bin.util.parser import Parser
from bin.util.loader import Loader


# 控制中心
class Pivot:
    __builder_import_path = Parser.parse_file_for_import('./bin/builder')  # builder 加载路径
    __builder_loaded = {}  # 已加载 builder 池
    __factory_import_path = Parser.parse_file_for_import('./bin/factory')  # factory 加载路径
    __factory_loaded = {}  # 已加载 factory 池
    __util_import_path = Parser.parse_file_for_import('./bin/util')  # util 加载路径
    __util_loaded = {'Parser': Parser, 'Loader': Loader} # 已加载 util 池

    # 通过给定类型寻找对应类
    def __get_class_from(self, class_type, class_name):
        # 1. 在以加载容器中寻找
        class_loaded = eval('self.__' + class_type + '_loaded')
        if class_name in class_loaded:
            return class_loaded[class_name]
        # 2. 寻找加载路径是否存在，如果存在则动态加载并加入已加载容器
        class_import_path = eval('self.__' + class_type + '_import_path')
        if class_name in class_import_path:
            target = Loader.load(class_import_path[class_name], class_name)
            class_loaded[class_name] = target
            return target
        # 3. 已加载容器和可加载路径中都没用发现类，跑出异常
        raise LookupError('{class_type} 中未发现 {class_name}'.format(
            class_type=class_type, class_name=class_name))

    # 获取 builder 类
    @classmethod
    def builder(cls, class_name):
        return cls.__get_class_from(cls, 'builder', class_name)

    # 获取 factory 类
    @classmethod
    def factory(cls, class_name):
        return cls.__get_class_from(cls, 'factory', class_name)

    # 获取 util 类
    @classmethod
    def util(cls, class_name):
        return cls.__get_class_from(cls, 'util', class_name)
