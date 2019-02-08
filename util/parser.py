import os


class Parser:
    """ 文本解释器 """

    @staticmethod
    def parse_slash_to_dot(target):
        """ 斜杠转点 """
        return target.replace(os.sep, '.')

    @staticmethod
    def parse_dash_to_dump(target):
        """ 下划线转驼峰 """
        return ''.join(map(lambda x: x.capitalize(), target.split('_')))
