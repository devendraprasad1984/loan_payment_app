import sys

from solution_using_class_based.app import commands
from solution_using_class_based.utils import utils


"""
Note: i was manually checking the logic and calculations, when loan was taken, payment was done, the output should be calculated based on remaining updated object
which was not happening, i checked for Harry in the last sample, here is my updated object for Harry
{'message': 'ledger -loan 2_2 belongs to customer 2 is taken from bank 2', 'data': {'_loan_id': '2_2', '_bank_id': '2', '_customer_id': '2', '_uid': 'dXFa_46h6AA', '_loan_amount': 10000.0, '_rate': 7.0, '_period': 3, '_emi_months': 26, '_total_interest': 2100, '_total_amount_pi': 12100.0, '_emi_amount': 336, '_emi_months_repaid': 10, '_repaid_amount': 5000.0, '_loan_amount_left': 7100.0}}
my output doesnt match with yours
"""
def main():
    args_length = sys.argv.__len__()
    util = utils.Utils()

    if args_length <= 1: return util.print_log('no input supplied')
    input_file_name = sys.argv[1]  # getting input filenames
    input_ledger_commands = util.read_input_file_contents(input_file_name)

    command = commands.Commands(input_ledger_commands)
    final_object = command.process_ledger_commands()
    # util.print_all_serialize(final_object['ledgers'])
    util.print_lists(final_object['output'])


if __name__ == "__main__":
    main()
