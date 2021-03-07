from fixed_monthly_payment import fixed_monthly_payment
import unittest


class TestFixedMonthlyPayment(unittest.TestCase):
    def test_1(self):
        balance = 3329
        annual_interest_rate = 0.2
        self.assertEqual(fixed_monthly_payment(balance, annual_interest_rate), 310, "Should be 310")
        print("Lowest Payment: 310")

    def test_2(self):
        balance = 4773
        annual_interest_rate = 0.2
        self.assertEqual(fixed_monthly_payment(balance, annual_interest_rate), 440, "Should be 440")
        print("Lowest Payment: 440")

    def test_3(self):
        balance = 3926
        annual_interest_rate = 0.2
        self.assertEqual(fixed_monthly_payment(balance, annual_interest_rate), 360, "Should be 360")
        print("Lowest Payment: 360")


if __name__ == '__main__':
    unittest.main()
