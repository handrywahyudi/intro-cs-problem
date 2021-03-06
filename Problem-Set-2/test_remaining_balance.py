from remaining_balance import remaining_balance
import unittest


class TestRemainingBalance(unittest.TestCase):
    def test1(self):
        balance = 484
        annual_interest_rate = 0.2
        monthly_payment_rate = 0.04
        self.assertEqual(remaining_balance(balance, annual_interest_rate, monthly_payment_rate), 361.61, "Should be 361.61")
        print("Remaining balance: 361.61")

    def test2(self):
        balance = 42
        annual_interest_rate = 0.2
        monthly_payment_rate = 0.04
        self.assertEqual(remaining_balance(balance, annual_interest_rate, monthly_payment_rate), 31.38, "Should be 31.38")
        print("Remaining balance: 31.38")

    def test3(self):
        balance = 72
        annual_interest_rate = 0.2
        monthly_payment_rate = 0.04
        self.assertEqual(remaining_balance(balance, annual_interest_rate, monthly_payment_rate), 53.79, "Should be 53.79")
        print("Remaining balance: 53.79")


if __name__ == '__main__':
    unittest.main()
