from solution_using_class_based.utils import enums


class PaymentHandler(enums.Enums):
    """handles payment related functions"""


    def __init__(self):
        pass


    def handle(self, data=None):
        super().handle(data, self.TYPE_PAYMENT)
