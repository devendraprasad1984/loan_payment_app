# from functools import wraps
from datetime import datetime

import sys


# solution to issue loans to customers from banks, display balances and get payment as monthly emis or bulk payment
# this solution will work in memory and wont be saved

TYPE_LOAN = 'LOAN'
TYPE_BALANCE = 'BALANCE'
TYPE_PAYMENT = 'PAYMENT'
TIMESTAMP_LOG_FORMAT = "%Y_%m_%d-%I:%M:%S_%p"


def print_log(args):
    print_time = datetime.now().strftime(TIMESTAMP_LOG_FORMAT)
    print(f'log {print_time}:', args)


def print_object_wrapper(param1=None, param2=None):
    return {'msg': param1, 'param': param2}


def read_input_file_contents(filename):
    f = open(filename, "r")
    file_contents = f.read().splitlines()
    f.close()
    return file_contents


def get_command_type(command):
    if command == TYPE_LOAN: return TYPE_LOAN
    if command == TYPE_BALANCE: return TYPE_BALANCE
    if command == TYPE_PAYMENT: return TYPE_PAYMENT


def process_ledger_commands(commands):
    for command in commands:
        command_key_words = command.split(' ')
        command_name = command_key_words[0]
        command_type = get_command_type(command_name)
        if command_type == TYPE_LOAN:
            if command_key_words.__len__() == 6:
                bank_name = command_key_words[1]
                customer_name = command_key_words[2]
                amount = command_key_words[3]
                no_of_years = int(command_key_words[4])
                rate_of_interest = float(command_key_words[5])
                print_log(f'processing loan for {customer_name} from {bank_name} for amount {amount} @ {rate_of_interest} for {no_of_years} years')
        if command_type == TYPE_PAYMENT:
            if command_key_words.__len__() == 5:
                bank_name = command_key_words[1]
                customer_name = command_key_words[2]
                emi_amount = float(command_key_words[3])
                no_of_emi = int(command_key_words[4])
                print_log(
                    f'processing payement by {customer_name} for loan taken '
                    f'from {bank_name}, an emi amount {emi_amount} and its '
                    f'{"per month" if no_of_emi == 1 else "lump sum"} payment that will '
                    f'reduce overall loan by {(no_of_emi * emi_amount).__str__()} and '
                    f'reduce remaining emis to'
                )
        if command_type == TYPE_BALANCE:
            if command_key_words.__len__() == 4:
                print('processing balance')


def handle_loan():
    pass


def handle_balance():
    pass


def handle_payment():
    pass


def main():
    # sys.argv[1] should give the absolute path to the input file
    input_file_name = sys.argv[1]
    # print_log(print_object_wrapper('input file content', input_file_name))
    input_ledger_commands = read_input_file_contents(input_file_name)
    # print_log(print_object_wrapper('input commands', input_ledger_commands))
    process_ledger_commands(input_ledger_commands)


if __name__ == "__main__":
    main()
