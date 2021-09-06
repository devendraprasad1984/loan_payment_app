import sys

from solution_using_class_based.utils import commands, utils


BANKS = []
CUSTOMERS = []
LEDGER = []


def print_all():
    """print all objects"""
    objects = [BANKS, CUSTOMERS, LEDGER]
    for obj in objects:
        print(obj, obj.serialize())


def main():
    args_length = sys.argv.__len__()
    util = utils.Utils()

    if args_length <= 1: return util.print_log('no input supplied')
    input_file_name = sys.argv[1]  # getting input filenames
    input_ledger_commands = util.read_input_file_contents(input_file_name)

    command = commands.Commands(input_ledger_commands)
    command.process_ledger_commands()


if __name__ == "__main__":
    main()
