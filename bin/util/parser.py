import os
import re


# 解析器
class Parser:
    __exclude = ['__init__.py']  # 排除规则
    __endwith = ['.py']  # 解析对象

    @classmethod
    def parse_file_for_import(cls, dir, endwith='default', exclude='default', append=True):
        """ 将指定目录下文件以 import 命名空间的形式输出到字典 """
        cls.__exclude_update(cls, exclude, append)  # 更新排除规则
        cls.__endwith_update(cls, endwith)  # 更新解析对象
        dir = os.path.relpath(dir)  # 路径转换成相对路径
        namespace = cls.parse_slash_to_dot(dir)  # 路径转命名空间

        result = {}
        for filename in os.listdir(dir):
            """ 遍历目标目录下的文件 """

            file_path = os.path.relpath('/'.join((dir, filename)))
            if os.path.isdir(file_path):
                """ 如果遍历对象是文件夹继续迭代 """
                result.update(cls.parse_file_for_import(file_path, endwith, exclude,append))

            if not cls.__check_exclude(cls, filename):
                """ 判断是否为排除对象 """
                suffix = cls.__check_endwith(cls, filename)
                if suffix:
                    """ 判断是否为解析对象 """
                    filename = filename[:-len(suffix)]
                    key = cls.parse_dash_to_dump(filename)
                    result[key] = '.'.join((namespace, filename))
        return result

    def __exclude_update(self, rule, is_append):
        """ 根据参数更新要忽略的内容 """
        if rule in (None, False, '', 'n', 'no', 'not', 'none'):
            self.__exclude = []
            return

        tmp = []
        if isinstance(rule, str):
            if rule == 'default':
                return
            tmp = rule.split(',')
        elif isinstance(rule, (tuple, list, set)):
            tmp = rule
        else:
            raise Exception(
                'exclude 参数必须为 str tuple list set 中的一种，当前值：{rule}'.format(rule))

        if is_append:
            """ 判断排除规则以什么形式添加 """
            self.__exclude.extend(tmp)
        else:
            self.__exclude = tmp

    def __endwith_update(self, rule):
        """ 根据条件更新需要解释的文件结尾形式 """
        if isinstance(rule, (tuple, set, list)):
            self.__endwith = rule
            return
        if isinstance(rule, str):
            self.__endwith = self.__endwith if rule == 'default' else rule.split(',')
            return
        raise TypeError(
            'endwith 参数必须为 str tuple list set 中的一种，当前值：{rule}'.format(rule))

    def __check_exclude(self, target):
        """ 检查目标是否需要排除 """
        for pattern in self.__exclude:
            pattern = pattern.replace('.',r'\.')
            pattern = pattern.replace('*', r'.*')
            if re.match(pattern, target) is not None:
                return True
        return False

    def __check_endwith(self, target):
        """ 检查目标是否以self.__endwith 中的一种结尾 """
        for endwith in self.__endwith:
            if target.endswith(endwith):
                return endwith
        else:
            return False

    @classmethod
    def parse_slash_to_dot(cls, target):
        """ 斜杠转点 """
        return target.replace(os.sep, '.')

    @classmethod
    def parse_dash_to_dump(cls, target):
        """ 下划线转驼峰 """
        return ''.join(map(lambda x: x.capitalize(), target.split('_')))


if __name__ == '__main__':
    parser = Parser()
    print(parser.parse_file_for_import(
        './bin/builder/', exclude='test.py', append=True))
