from datetime import datetime, timedelta, date


class Dater:
    """ 字符串日期工具 """

    @staticmethod
    def today(fmt='%Y%m%d'):
        return datetime.strftime(datetime.today(), fmt)

    @staticmethod
    def year_end(date1='', fmt='%Y%m%d'):
        tt = datetime.today() if date1 == '' else datetime.strptime(date1, fmt)
        return datetime.strftime(date(tt.year, 12, 31), fmt)

    @staticmethod
    def month_end(date1='', fmt='%Y%m%d'):
        tt = datetime.today() if date1 == '' else datetime.strptime(date1, fmt)
        year = tt.year
        month = tt.month + 1
        if tt.month == 12:
            year += 1
            month = 1
        tt = date(year, month, 1) + timedelta(days=-1)
        return datetime.strftime(tt, fmt)

    @staticmethod
    def isin_same_month(date1, date2, fmt='%Y%m%d'):
        if type(date1)==str and type(date2)==str:
            tt1 = datetime.strptime(date1, fmt)
            tt2 = datetime.strptime(date2, fmt)
            if tt1.year == tt2.year:
                return tt1.month == tt2.month
        return False

    @staticmethod
    def isin_same_week(date1, date2, fmt='%Y%m%d'):
        if type(date1)==str and type(date2)==str:
            tt1 = datetime.strptime(date1, fmt)
            tt2 = datetime.strptime(date2, fmt)
            if tt1.year == tt2.year:
                return tt1.isocalendar()[1] == tt2.isocalendar()[1]
        return False

    @staticmethod
    def offset(date1, offset, fmt='%Y%m%d'):
            if date1:
                return datetime.strftime(datetime.strptime(date1, fmt) + timedelta(days=offset), fmt)
            return ''