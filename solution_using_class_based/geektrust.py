import sys

from solution_using_class_based.app import commands
from solution_using_class_based.utils import utils


def print_all(listOfObjects: []):
    """print objects via their serialize call"""
    if listOfObjects.__len__() == 0: return
    util = utils.Utils()
    for obj in listOfObjects:
        msg = {"message": obj.__str__(), "data": obj.serialize()}
        util.print_log(**msg)


def main():
    args_length = sys.argv.__len__()
    util = utils.Utils()

    if args_length <= 1: return util.print_log('no input supplied')
    input_file_name = sys.argv[1]  # getting input filenames
    input_ledger_commands = util.read_input_file_contents(input_file_name)

    command = commands.Commands(input_ledger_commands)
    final_object = command.process_ledger_commands()
    print_all(final_object['ledgers'])
    # print_all(final_object['banks'])
    # print_all(final_object['customers'])
    # print_all(final_object['output'])



if __name__ == "__main__":
    main()
