from .database import BasicDatabase
import pymysql

class Mysql(BasicDatabase):
  '''
  BasicDatabase 的子类 使用pymysql实现数据库连接
  '''
  cur = None

  # connection 不存在时建立新的 connection,否则返回已有 connection
  def connection(self, **args):
    if self.conn == None :
      self.connect(**args)
    return self.conn

  # 使用 pymysql 实现与 mysql 的连接,可传入自定义参数覆盖默认的 config 配置参数
  def connect(self, **args):
    self.set(**args)
    self.conn = pymysql.connect(host     = self.host,
                                user     = self.user,
                                password = self.password,
                                database = self.database,
                                charset  = self.charset)
    return self.conn

  # cursor 不存在时建立新的 cursor,否则返回已有 cursor
  def cursor(self):
    if self.cur == None :
      self.cur = self.connection().cursor()
    return self.cur

  # 封装 pymysql 直接执行sql,自动实现 pymysql.connect().cursor().execute() 操作
  def exec(self, sql):
    super().exec(sql)
    result = None
    try:
      result = self.cursor().execute(sql)
    except Exception as e:
      print("sql = '{0}'\n{1}".format(self.sql, e))
      return result
    else:
      self.connection().commit()
    finally:
      self.cursor().close()
      self.connection().close()
      return result