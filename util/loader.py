import os
from util.parser import Parser


class Loader:
    """ 类加载器 """

    @staticmethod
    def load_class_from_dir(path, exclude='__init__.py'):
        """ 加载指定目录下按下划线转驼峰法命名的文件中的类 """
        relpath = os.path.relpath(path)
        result = {}
        for filename in os.listdir(relpath):
            if filename.endswith('.py') and filename != exclude:
                filename = filename[:-3]
                filepath = os.sep.join((relpath, filename))
                namespace = Parser.parse_slash_to_dot(filepath)
                classname = Parser.parse_dash_to_dump(filename)
                module = __import__(namespace, fromlist=True)
                result[classname] = getattr(module, classname)
        return result
