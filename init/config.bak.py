# 数据库参数,请根据自己使用的数据库进行设置
database_settings = {
    'mysql' : {
    	'type'     : 'mysql',
    	'port'     : 3306,
    	'host'     : 'localhost',
    	'user'     : 'root',
    	'password' : 'your database password',
    	'database' : 'stock',
        'charset'  : 'utf8'
    }
}

# tushare.pro 接口token
tushare_settings = {
    'ts_token': 'your tushare.pro token'
}