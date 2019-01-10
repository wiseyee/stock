'''
项目配置信息,需根据用户自己的环境配置相应参数
'''
# 数据库设置
database_setting = {
    # 选择要使用的数据库类型,例如 "mysql sqlite 等"
    'type'  : 'mysql',
    # mysql 数据库配置信息
    'mysql' : {
        'port'      : 3306,
        'host'      : 'localhost',
        'user'      : 'root',
        'password'  : 'your database password',
        'db_name'   : 'stock',
        'encoding'  : 'utf-8'
    }
}

# tushare 设置
tushare_setting = {
    'token' : 'your tushare pro_api token'
}