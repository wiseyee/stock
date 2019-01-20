import os


# 解释器
class Parser:
    __exclude = ('__init__.py')  # 解释器要忽略的内容

    @classmethod
    def parse_file_for_import(cls, dir, exclude='default', endwith='.py', expand_dir=True):
        """ 将指定目录下文件以 import 命名空间的形式输出到字典 """
        cls.__exclude = cls.__update_exclude(cls, exclude=exclude)
        namespace = dir[2:] if str(dir).startswith('./') else dir
        namespace = namespace[:-1] if namespace.endswith('/') else namespace
        namespace = namespace.replace('/', '.')
        result = {}
        for filename in os.listdir(dir):
            tmp_dir = '/'.join((dir.rstrip('/'), filename))
            if expand_dir and os.path.isdir(tmp_dir):
                result.update(cls.parse_file_for_import(tmp_dir))
            if filename.endswith(endwith) and not filename in cls.__exclude:
                filename = filename[:-3]
                key = cls.parse_dash_to_dump(filename)
                result[key] = '.'.join((namespace, filename))
        return result

    def __update_exclude(self, exclude):
        """ 根据参数更新要忽略的内容 """
        if exclude == 'default':
            return self.__exclude
        if exclude in (None, '', False):
            return []
        if exclude is str:
            self.namespace_exclude = str(exclude).split(',')
            return
        if isinstance(exclude, (tuple, list, set)):
            self.__exclude = exclude
            return
        raise Exception('exclude 参数必须为 str tuple list set 中的一种')

    @classmethod
    def parse_dash_to_dump(cls, target):
        """ 下划线字符串转驼峰命名 """
        return ''.join(map(lambda x: x.capitalize(), target.split('_')))


if __name__ == '__main__':
    parser = Parser()
    # print(parser.parse_dash_to_dump('database'))
    # print('bin/factories'.split('/'))
    print(parser.parse_file_for_import('./bin/builder/'))
