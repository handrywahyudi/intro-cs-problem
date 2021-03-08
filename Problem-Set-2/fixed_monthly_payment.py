# Problem Set 2
# Problem 2: https://bit.ly/3bp6sfW

def fixed_monthly_payment(balance, annual_interest_rate):
    current_balance = balance
    fixed_payment = 10
    monthly_interest_rate = annual_interest_rate / 12.0
    while current_balance > 0:
        current_balance = balance
        for month in range(12):
            current_balance -= fixed_payment
            current_balance += (monthly_interest_rate * current_balance)
        if current_balance > 0:
            fixed_payment += 10

    return fixed_payment


if __name__ == "__main__":
    print(fixed_monthly_payment(4773, 0.2))
