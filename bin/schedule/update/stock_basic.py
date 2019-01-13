def update(engine, ts, data, table):
    '''
    1. get data from tushare
    2. use the tushare.to_sql func to update data to table
    '''
    print(' first using {ts} to get data then using {session} to update database'.format(ts = ts, session = session))