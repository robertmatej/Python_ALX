'''
Cash Machine do wpłacania i wypłacania pieniędzy

'''

class CashMachine():

    def __init__(self):
        self.bills = []
        self.broken = False

#    @property
    def is_available(self):
        return bool(self.bills)

    def put_money(self, bills):
        self.bills.extend(bills)
        return self.bills

    def withdraw_money(self, ammount):
        bills_to_withdraw = []
        for bill in sorted(self.bills, reverse=True):
            if sum(bills_to_withdraw)+bill <= ammount:
                bills_to_withdraw.append(bill)

            if sum(bills_to_withdraw)==ammount:
                for bill in bills_to_withdraw:
                    self.bills.remove(bill)
                return bills_to_withdraw
            return []

def test_cash_machine_is_available():
    cash_machine = CashMachine()
    assert cash_machine.is_available() == False

#def test_cash_mashine_is_available_after_put_money():

def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200,100,100,50])
    assert cash_machine.is_available() == True

def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100,50]
    assert cash_machine.withdraw_money(150) == []

def test_cash_machine_wrong_ammount():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(90) == []

def test_cash_machine_order_matter():
    cash_machine = CashMachine()
    cash_machine.put_money([20, 20, 50, 50])
    assert cash_machine.withdraw_money(100) == [50,50]


#def test_cash_machine_is_not_alailable_after_withdrawal_all_money():

def test_cash_machine_is_not_broken():
    cash_machine = CashMachine()
    assert not cash_machine.is_available
