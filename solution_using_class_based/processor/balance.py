from solution_using_class_based.processor.process_handler import ProcessHandler
from solution_using_class_based.utils import enums


class BalanceHandler(enums.Enums, ProcessHandler):
    """handles balance related functions"""


    def __init__(self):
        pass


    def handle(self, **kwargs):
        super().handle(self.TYPE_BALANCE, kwargs)
