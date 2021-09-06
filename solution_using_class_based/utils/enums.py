class Enums():
    """holds the enum/constants to be used across application"""
    key_object = 'object'
    key_id = 'id'
    key_uid = 'uid'
    key_name = 'name'
    key_limit = 'loan_limit'
    key_loan = 'loan_id'
    key_customer_id = 'customer_id'
    key_customer_name = 'customer_name'
    key_bank_id = 'bank_id'
    key_bank_name = 'bank_name'
    key_emi_months = 'emi_months'
    key_emi_months_repaid = 'emi_months_repaid'
    key_loan_amount = 'loan_amount'
    key_emi_amount = 'emi_amount'
    key_rate = 'rate'
    key_period = 'period'
    key_interest = 'interest'
    key_repaid_amount = 'repaid_amount'
    key_total_amount_pi = 'total_amount_pi'
    key_when = 'when'
    key_active = 'active'
    key_found = 'found'

    TYPE_LOAN = 'LOAN'
    TYPE_BALANCE = 'BALANCE'
    TYPE_PAYMENT = 'PAYMENT'
    TIMESTAMP_LOG_FORMAT = "%Y_%m_%d-%I:%M:%S_%p"
    BANKS = []
    CUSTOMERS = []
    LEDGER = []
    DEFAULT_CUSTOMER_LOAN_LIMIT = 10000000
    PRINT_LOG_WITH_TIMESTAMP = False
