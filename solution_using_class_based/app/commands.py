from solution_using_class_based.factory.command_handler import CommandHandlerFactory
from solution_using_class_based.models import bank, customer
from solution_using_class_based.utils import checkers, enums


class Commands(enums.Enums, checkers.Checker):
    """processing commands logic"""
    handler = None
    _BANKS = []
    _CUSTOMERS = []
    _LOANS = []


    def __init__(self, commands=None):
        self.commands = commands


    def _add_bank_if_missing(self, name):
        # hold bank details
        found, id = self.check_present_of_same_name_object(self._BANKS, name)
        if id == -1:
            id = self._BANKS.__len__() + 1
            self._BANKS.append(bank.Bank(id=id, name=name))
        return id


    def _add_customer_if_missing(self, name):
        # hold customer details
        found, id = self.check_present_of_same_name_object(self._CUSTOMERS, name)
        if id == -1:
            id = self._CUSTOMERS.__len__() + 1
            self._CUSTOMERS.append(customer.Customer(id=id, name=name))
        return id


    def process_ledger_commands(self):
        for cmd in self.commands:
            if cmd == '': continue
            command_keys = cmd.split(' ')
            bank_name = command_keys[1]
            customer_name = command_keys[2]

            bank_id = self._add_bank_if_missing(name=bank_name)
            customer_id = self._add_customer_if_missing(name=customer_name)
            loan_id = f'{bank_id}_{customer_id}'
            # process and handle command LOAN, PAYMENT, BALANCE
            command_handler = CommandHandlerFactory(type=command_keys[0]).get()
            params = {
                self.key_command: command_keys,
                self.key_loan: loan_id,
                self.key_loan_object: self._LOANS
            }
            command_handler.handle(**params)
            self._LOANS = command_handler.processed_loan_object()

        return {
            'banks': self._BANKS,
            'customers': self._CUSTOMERS,
            'ledgers': self._LOANS,
        }
