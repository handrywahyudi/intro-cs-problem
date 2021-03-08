from fixed_monthly_bisection_search import fixed_monthly_payment
import unittest


class TestFixedMonthlyPayment(unittest.TestCase):
    def test1(self):
        balance = 320000
        annual_interest_rate = 0.2
        self.assertEqual(fixed_monthly_payment(balance, annual_interest_rate), 29157.09, "Should be 29157.09")
        print("Lowest payment: 29157.09")

    def test2(self):
        balance = 999999
        annual_interest_rate = 0.18
        self.assertEqual(fixed_monthly_payment(balance, annual_interest_rate), 90325.02, "Should be 90325.02")
        print("Lowest payment: 90325.02")

    def test3(self):
        balance = 1000000
        annual_interest_rate = 0.2
        self.assertEqual(fixed_monthly_payment(balance, annual_interest_rate), 91115.91, "Should be 91115.91")
        print("Lowest payment: 91115.91")


if __name__ == '__main__':
    unittest.main()
