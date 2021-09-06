from solution_using_class_based.models import bank, customer, ledger
from solution_using_class_based.processor import balance, loan, payment
from solution_using_class_based.utils import checkers, enums


class Commands(enums.Enums, checkers.Checker):
    """processing commands logic"""
    handler = None
    _BANKS = []
    _CUSTOMERS = []
    _LEDGER = []
    prepared_objects = {}


    def __init__(self, commands=None):
        self.commands = commands


    def _get_command_handler(self, command):
        if command == self.TYPE_LOAN: return loan.LoanHandler()
        if command == self.TYPE_BALANCE: return balance.BalanceHandler()
        if command == self.TYPE_PAYMENT: return payment.PaymentHandler()


    def _add_bank_if_missing(self, name):
        # hold bank details
        if self.check_present_of_same_name_object(self._BANKS, name) == False:
            self._BANKS.append(bank.Bank(id=self._BANKS.__len__() + 1, name=name))


    def _add_customer_if_missing(self, name):
        # hold customer details
        if self.check_present_of_same_name_object(self._CUSTOMERS, name) == False:
            self._CUSTOMERS.append(customer.Customer(id=self._CUSTOMERS.__len__() + 1, name=name))


    def process_ledger_commands(self):
        for cmd in self.commands:
            if cmd == '': continue
            command_keys = cmd.split(' ')
            bank_name = command_keys[1]
            customer_name = command_keys[2]

            self._add_bank_if_missing(name=bank_name)
            self._add_customer_if_missing(name=customer_name)
            self._LEDGER.append(ledger.Ledger(id=self._LEDGER.__len__(), name=customer_name))

            # process and handle command LOAN, PAYMENT, BALANCE
            command_handler = self._get_command_handler(command_keys[0])
            command_handler.handle()

        self.prepared_objects = {
            'banks': self._BANKS,
            'customers': self._CUSTOMERS,
            'ledgers': self._LEDGER,
        }
        return self.prepared_objects
