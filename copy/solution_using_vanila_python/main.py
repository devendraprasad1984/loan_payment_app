# from functools import wraps
from datetime import datetime

import sys


# solution to issue loans to customers from banks, display balances and get payment as monthly emis or bulk payment
# this solution will work in memory and wont be saved

TYPE_LOAN = 'LOAN'
TYPE_BALANCE = 'BALANCE'
TYPE_PAYMENT = 'PAYMENT'


def print_log(args):
    print_time = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
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
        command_key_words=command.split(' ')
        command_name=command_key_words[0]
        command_type=get_command_type(command_name)
        if command_type==TYPE_LOAN:
            if command_key_words.__len__()==6:
                print('processing loan')
        if command_type==TYPE_PAYMENT:
            if command_key_words.__len__()==5:
                print('processing payment')
        if command_type==TYPE_BALANCE:
            if command_key_words.__len__()==4:
                print('processing balance')

        print_log(command_key_words)


def handle_loan():
    pass


def handle_balance():
    pass


def handle_payment():
    pass


def main():
    # sys.argv[1] should give the absolute path to the input file
    input_file_name = sys.argv[1]
    print_log(print_object_wrapper('input file content', input_file_name))
    input_ledger_commands = read_input_file_contents(input_file_name)
    print_log(print_object_wrapper('input commands', input_ledger_commands))
    process_ledger_commands(input_ledger_commands)


if __name__ == "__main__":
    main()
