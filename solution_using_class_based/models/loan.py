from solution_using_class_based.utils import enums, utils


class Loan(enums.Enums):
    """store ledger entity details"""
    _loan_id = None
    _uid = None
    _customer_id = None
    _bank_id = None
    _emi_months = None
    _emi_months_repaid = 0
    _loan_amount = None
    _emi_amount = None
    _rate = None
    _period = None
    _interest = None
    _repaid_amount = 0
    _total_amount_pi = None
    _active = None
    _no_of_years = None
    _total_interest = None


    def __init__(self,
                 id=None,
                 loan_amount=None,
                 rate=None,
                 period=None,
                 interest=None,
                 ):
        """initialize the fields"""
        self._loan_id = id  # eg 1_1, <bankid>_<customerid>
        self._bank_id = id.split('_')[0]  #
        self._customer_id = id.split('_')[1]
        self._uid = utils.Utils(8).get_secret_key()

        self._loan_amount = loan_amount
        self._rate = rate
        self._period = period
        self._interest = interest


    def calculate(self):
        self._emi_months = self._period * 12
        self._total_interest = round(self._amount * self._period * self._rate_of_interest / 100)
        self._total_amount_pi = self._amount + self._total_interest
        self._emi_amount = round(self._total_amount_pi / self._emi_months)


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
            self.key_period: self._period,
            self.key_interest: self._total_interest,
            self.key_repaid_amount: self._repaid_amount,
            self.key_total_amount_pi: self._total_amount_pi,
            self.key_when: utils.Utils().get_timestamp(),
            self.key_active: self._active,
            self.key_uid: self._uid,
        }
