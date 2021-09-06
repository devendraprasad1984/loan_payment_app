from solution_using_class_based.utils import enums, utils


class Ledger(enums.Enums):
    """store ledger entity details"""
    _loan_id = None
    _uid = None
    _customer_id = None
    _bank_id = None
    _emi_months = None
    _emi_months_repaid = None
    _loan_amount = None
    _emi_amount = None
    _rate = None
    _period = None
    _interest = None
    _repaid_amount = None
    _total_amount_pi = None
    _active = None
    _rate_of_interes = None
    _no_of_years = None
    _total_interest = None


    def __init__(self, id):
        """initialize the fields"""
        self._loan_id = id
        self._uid = utils.Utils(8).get_secret_key()


    def __str__(self):
        return f'ledger -loan {self._loan_id} belongs to customer {self._customer_id} is taken from bank {self._bank_id}'


    def serialize(self):
        return {
            self.key_loan: self._loan_id,
            self.key_customer_id: self._customer_id,
            self.key_bank_id: self._bank_id,
            self.key_emi_months: self._emi_months,
            self.key_emi_months_repaid: self._emi_months_repaid,
            self.key_loan_amount: self._loan_amount,
            self.key_emi_amount: self._emi_amount,
            self.key_rate: self.rate_of_interest,
            self.key_period: self._no_of_years,
            self.key_interest: self._total_interest,
            self.key_repaid_amount: self._repaid_amount,
            self.key_total_amount_pi: self._total_amount_pi,
            self.key_when: utils.Utils().get_timestamp(),
            self.key_active: self._active,
        }
