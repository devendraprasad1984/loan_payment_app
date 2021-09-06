from solution_using_class_based.processor import balance, loan, payment
from solution_using_class_based.utils import enums


class Commands(enums.Enums):
    """processing commands logic"""
    handler=None

    def __init__(self, commands=None):
        self.commands = commands


    def _get_command_handler(self):
        if self.command == self.TYPE_LOAN: return loan.LoanHandler()
        if self.command == self.TYPE_BALANCE: return balance.BalanceHandler()
        if self.command == self.TYPE_PAYMENT: return payment.PaymentHandler()


    def process_ledger_commands(self):
        for cmd in self.commands:
            if cmd == '': continue
            command_keys = cmd.split(' ')
            command_handler = self._get_command_handler(command_keys[0])
            command_handler(command_keys)
