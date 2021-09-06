import sys

from solution_using_class_based.utils import commands, utils


def print_all(final_object: {}):
    """print all objects, BANKS, CUSTOMERS, LEDGERS"""
    if final_object.__len__() == 0: return
    for obj in final_object.values():
        print(obj.__str__(), obj.serialize())


def main():
    args_length = sys.argv.__len__()
    util = utils.Utils()

    if args_length <= 1: return util.print_log('no input supplied')
    input_file_name = sys.argv[1]  # getting input filenames
    input_ledger_commands = util.read_input_file_contents(input_file_name)

    command = commands.Commands(input_ledger_commands)
    final_object = command.process_ledger_commands()
    print_all(final_object=final_object)


if __name__ == "__main__":
    main()
