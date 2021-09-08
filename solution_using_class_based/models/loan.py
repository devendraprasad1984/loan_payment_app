from solution_using_class_based.serializers.iSerialize import ISerialize
from solution_using_class_based.utils import enums, utils


class Loan(enums.Enums, ISerialize):
    """store loan ledger entity details"""

    _loan_id = -1
    _uid = None
    _customer_id = None
    _bank_id = None
    _emi_months = 0
    _emi_months_repaid = 0
    _loan_amount = 0
    _emi_amount = 0
    _rate = 0
    _period = 0
    _interest = 0
    _repaid_amount = 0
    _total_amount_pi = 0
    _loan_amount_left = 0
    _active = True
    _no_of_years = 0
    _total_interest = None


    def __init__(self,
                 id=None,
                 loan_amount=None,
                 rate=None,
                 period=None,
                 ):
        """initialize the fields"""
        ids_arr = id.split('_')
        self._loan_id = id  # eg 1_1, <bankid>_<customerid>
        self._bank_id = ids_arr[0]  #
        self._customer_id = ids_arr[1]
        self._uid = utils.Utils(8).get_secret_key()

        self._loan_amount = float(loan_amount)
        self._rate = float(rate)
        self._period = int(period)


    def calculate(self):
        """calculate few parameters based on input given for loan processing"""
        self._emi_months = self._period * 12
        self._total_interest = round(self._loan_amount * self._period * self._rate / 100)
        self._total_amount_pi = float(self._loan_amount + self._total_interest)
        self._emi_amount = round(self._total_amount_pi / self._emi_months)
        return self


    def update(self, lump_sum_payment=0, emi_months=0):
        """update loan object with lumpsum payment from emi_months"""
        self._emi_months_repaid += int(emi_months)
        self._emi_months -= int(emi_months)
        self._repaid_amount = self._repaid_amount + float(lump_sum_payment)
        self._loan_amount_left = self._total_amount_pi - float(lump_sum_payment)
        return self


    def get_bank_id(self):
        return self._bank_id


    def get_loan_id(self):
        return self._loan_id


    def get_customer_id(self):
        return self._customer_id


    def __str__(self):
        return f'ledger -loan {self._loan_id} belongs to customer {self._customer_id} is taken from bank {self._bank_id}'


    def serialize(self):
        return self.__dict__
        # return {
        #     self.key_loan: self._loan_id,
        #     self.key_customer_id: self._customer_id,
        #     self.key_bank_id: self._bank_id,
        #     self.key_emi_months: self._emi_months,
        #     self.key_emi_months_repaid: self._emi_months_repaid,
        #     self.key_loan_amount: self._loan_amount,
        #     self.key_emi_amount: self._emi_amount,
        #     self.key_period: self._period,
        #     self.key_interest: self._total_interest,
        #     self.key_repaid_amount: self._repaid_amount,
        #     self.key_total_amount_pi: self._total_amount_pi,
        #     self.key_when: utils.Utils().get_timestamp(),
        #     self.key_active: self._active,
        #     self.key_uid: self._uid,
        # }
