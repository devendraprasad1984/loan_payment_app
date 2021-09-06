import sys

from solution_using_class_based.utils import commands, utils


BANKS = []
CUSTOMERS = []
LEDGER = []


def get_banks():
    for _ in BANKS:
        print(_.serialize())


def get_customers():
    for _ in CUSTOMERS:
        print(_.serialize())


def get_ledgers():
    for _ in LEDGER:
        print(_.serialize())


def main():
    args_length = sys.argv.__len__()
    util = utils.Utils()

    if args_length <= 1: return util.print_log('no input supplied')
    input_file_name = sys.argv[1]  # getting input filenames
    input_ledger_commands = util.read_input_file_contents(input_file_name)

    command = commands.Commands(input_ledger_commands)
    command.process_ledger_commands(input_ledger_commands)


if __name__ == "__main__":
    main()
