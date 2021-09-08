from solution_using_class_based.processor.process_handler import ProcessHandler
from solution_using_class_based.utils import enums


class LoanHandler(enums.Enums, ProcessHandler):
    """handles loan related functions"""

    def __init__(self):
        pass


    def handle(self, data=None):
        super().handle(data, self.TYPE_LOAN)
