import sys

from solution_using_class_based.models.bank import Bank


def main():
    args_length = sys.argv.__len__()
    banks=Bank('IDIDI')
    print(banks.serialize())
    # if args_length <= 1: return print_log('no input supplied')
    # input_file_name = sys.argv[1]  # getting input filenames
    # input_ledger_commands = read_input_file_contents(input_file_name)
    # process_ledger_commands(input_ledger_commands)
    # print_base_objects()

if __name__ == "__main__":
    main()


