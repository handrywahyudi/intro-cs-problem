def remaining_balance(balance, annual_interest_rate, monthly_payment_rate):
    # For month 0
    minimum_payment = balance * monthly_payment_rate
    unpaid_balance = balance - minimum_payment
    interest = annual_interest_rate / 12.0 * unpaid_balance
    balance = unpaid_balance + interest

    # For month 1 to 12
    for month in range(12):
        minimum_payment = balance * monthly_payment_rate
        unpaid_balance = balance - minimum_payment
        interest = annual_interest_rate / 12.0 * unpaid_balance
        print("Month " + str(month + 1) + " Remaining balance: %.2f" % balance)
        balance = unpaid_balance + interest


if __name__ == "__main__":
    balance = 484
    annual_interest_rate = 0.2
    monthly_payment_rate = 0.04
    remaining_balance(balance, annual_interest_rate, monthly_payment_rate)
