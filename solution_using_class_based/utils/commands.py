from solution_using_class_based.processor import balance, loan, payment
from solution_using_class_based.utils import enums


class Commands(enums.Enums):
    """processing commands logic"""
    handler = None
    bank_name = None
    customer_name = None
    BANKS = []
    CUSTOMERS = []
    LEDGER = []
    prepared_objects = {}


    def __init__(self, commands=None):
        self.commands = commands


    def _get_command_handler(self, command):
        if command == self.TYPE_LOAN: return loan.LoanHandler()
        if command == self.TYPE_BALANCE: return balance.BalanceHandler()
        if command == self.TYPE_PAYMENT: return payment.PaymentHandler()


    def process_ledger_commands(self):
        for cmd in self.commands:
            if cmd == '': continue
            command_keys = cmd.split(' ')
            self.bank_name = command_keys[1]
            self.customer_name = command_keys[2]
            print(self.bank_name, self.customer_name)
            command_handler = self._get_command_handler(command_keys[0])
            command_handler.handle()

        self.prepared_objects = {
            'banks': self.BANKS,
            'customers': self.CUSTOMERS,
            'ledgers': self.LEDGER,
        }
        return self.prepared_objects
