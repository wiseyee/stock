import tushare
from conf.config import setting


tushare_pro = tushare.pro_api(setting['tushare']['token'])
