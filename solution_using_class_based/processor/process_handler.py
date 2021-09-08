# from abc import ABC, abstractmethod
from solution_using_class_based.utils.enums import Enums


class ProcessHandler(Enums):
    """common data handling logic"""
    _this_loan_object = None
    _this_command = None
    _this_loan_id = None


    def handle(self, type=None, **kwargs):
        """handle derived classes handler logic"""
        self._this_loan_object = kwargs[self.key_loan_object]
        self._this_command = kwargs[self.key_command]
        self._this_loan_id = kwargs[self.key_loan]

        print(f'from child {type} - {kwargs}')
