from data.db import session
from data.model.update_record import UpdateRecord
from util.dater import Dater


# 更新数据表前后操作
def record_update(model):
    def wrapper(fn):
        def inner_wrapper(*args, **kargs):
            # 如果记录中对应表近日已更新直接返回
            record = session.query(model).filter(
                UpdateRecord.table == model.__tablename__).first()
            if record and record.last_updating == Dater.today():
                return
            # 执行被包装的表更新任务
            fn(*args, **kargs)
            # 表更新完毕在记录更新日期的表中修改最近更新日期
            if record:
                record.last_updating = Dater.today()
            else:
                record = UpdateRecord(table=model.__tablename__,
                                      last_updating=Dater.today())
                session.add(record)
            session.commit()
        return inner_wrapper
    return wrapper
