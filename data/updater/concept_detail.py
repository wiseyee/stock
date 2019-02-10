import time
import pandas as pd
from data.db import engine, session
from data.api import tushare_pro as api
from data.model.concept import Concept
from data.model.concept_detail import ConceptDetail
from data.updater.wrapper import record_update
from util.logger import Logger
from util.dater import Dater


class ConceptDetailUpdater:
    """ concept_detail 数据更新器 """

    @record_update(model=ConceptDetail)
    def start(self):
        # 获得本地 concept 列表
        db_data = pd.read_sql_table('concept', engine)
        if db_data.empty:
            return

        # 根据 concept 列表获取相应的股票概念明细
        ta_data = pd.DataFrame()
        for code in db_data['code'].tolist():
            ts_data = self.__get_data(code)
            if not ts_data.empty:
                ts_data.rename(columns={'id': 'code'}, inplace=True)
                ta_data = pd.concat([ta_data, ts_data], ignore_index=True)

        if not ta_data.empty:
            ta_data.to_sql('concept_detail', engine,
                           if_exists='replace', index_label='id')

    def __get_data(self, code, i=0):
        """ 获得指定概念代号的股票明细 """
        ts_data = pd.DataFrame()
        # 10 次请求不成功，记录警告
        if i > 10:
            Logger.warning(
                'Request of tushare api concept_detail() interface has failed more than 10 times')
            return
        # 尝试请求 api ，并捕获异常
        try:
            ts_data = api.concept_detail(id=code)
        except Exception:
            Logger.info(
                'Request of tushare api concept_detail() interface timeout try after 60s')
            time.sleep(60)
            return self.__get_data(code, i+1)
        # 返回 api 数据
        return ts_data
