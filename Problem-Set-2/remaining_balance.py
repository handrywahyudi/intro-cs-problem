# Problem Set 2
# Problem 1: https://bit.ly/3kTczMF
def remaining_balance(balance, annual_interest_rate, monthly_payment_rate):
    remaining = 0.0
    for month in range(12):
        minimum_payment = balance * monthly_payment_rate
        unpaid_balance = balance - minimum_payment
        interest = annual_interest_rate / 12.0 * unpaid_balance
        balance = unpaid_balance + interest
        remaining = round(balance, 2)

    return remaining


if __name__ == "__main__":
    balance = 42
    annual_interest_rate = 0.2
    monthly_payment_rate = 0.04
    print(remaining_balance(balance, annual_interest_rate, monthly_payment_rate))