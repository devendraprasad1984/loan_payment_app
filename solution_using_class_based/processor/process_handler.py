# from abc import ABC, abstractmethod
from solution_using_class_based.models.loan import Loan
from solution_using_class_based.utils.enums import Enums


class ProcessHandler(Enums):
    """common data handling logic"""
    _this_loan_object = None
    _this_command = None
    _this_loan_id = None
    _this_command_type = None


    def handle(self, type=None, **kwargs):
        """handle derived classes handler logic"""
        self._this_command_type = type
        self._this_loan_object = kwargs[self.key_loan_object]
        self._this_command = kwargs[self.key_command]
        self._this_loan_id = kwargs[self.key_loan]

        # print(f'from child {self._this_command_type} - {self._this_loan_id} - {self._this_command} - {self._this_loan_object}')
        self._process_loan()
        self._process_payment()
        self._process_balance()


    def _process_loan(self):
        """processing loan query"""
        if self._this_command_type != self.TYPE_LOAN: return

        _loan_amount = self._this_command[3]
        _no_of_years = self._this_command[4]
        _rate = self._this_command[5]
        _this = Loan(
            id=self._this_loan_id,
            loan_amount=_loan_amount,
            rate=_rate,
            period=_no_of_years,
        ).calculate()
        self._this_loan_object.append(_this)
        pass


    def _process_balance(self):
        """processing balance query"""
        if self._this_command_type != self.TYPE_BALANCE: return
        pass


    def _process_payment(self):
        """processing payment query"""
        if self._this_command_type != self.TYPE_PAYMENT: return
        pass


    def processed_loan_object(self):
        """return final modified processed loan object having updated values for loan, balance and payment queries"""
        return self._this_loan_object
