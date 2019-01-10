from conf.config import database_setting as db
from db.tables import init_all_tables
import threading

class Project():
    def __init__(self):
        self.session = init_all_tables(db)

    def run_schedule(self):
        pass

    def run_strategy(self):
        pass

    def run(self):
        pass

        