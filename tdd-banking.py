import unittest

class Banking():
    def __init__(self):
        self.balance = 0

    def credit(self, amount):
        amount_type = (int, float, complex)
        if isinstance(amount, amount_type):
            self.balance += amount
            return self.balance
        else:
            print("raises error")
            raise ValueError

    def debit(self, amount):
        amount_type = (int, float, complex)

        if isinstance(amount, amount_type):
            self.balance -= amount
            return self.balance
        else:
            raise ValueError

"""
    def credit(self,amount):
        #pass
        self.balance += amount;
        return self.balance
"""


class testBanking(unittest.TestCase):

    def setUp(self):
        self.bank = Banking()

    def test_banking_credit_method_return_correct_result(self):
        final_bal = self.bank.credit(1000)
        self.assertEqual(1000,final_bal)

    def test_banking_credit_method_returns_error_if_args_not_numbers(self):
        self.assertRaises(ValueError, self.bank.credit, "one")

    def test_banking_debit_method_returns_correct_result(self):
        final_bal = self.bank.debit(700)
        self.assertEqual(-700, final_bal)

    def test_banking_debit_method_returns_error_if_args_not_numbers(self):
        self.assertRaises(ValueError, self.bank.debit, 'three')

if __name__ == '__main__':
    unittest.main()
