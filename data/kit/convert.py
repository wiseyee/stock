import pandas as pd


def record_to_dataframe(records):
    """ sqlalchemy session query result to dataframe """
    data = {}
    if records:
        if not isinstance(records, list):
            records = [records]
        # generate column index
        for k in records[0].__dict__:
            if k != '_sa_instance_state':
                data[k] = []
        # generate data
        for row in records:
            for k in data:
                data[k].append(row.__dict__[k])
    return pd.DataFrame(data)
