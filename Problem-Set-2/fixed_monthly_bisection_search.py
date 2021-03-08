# Problem Set 2
# Problem 3: https://bit.ly/2OtXsNy

def fixed_monthly_payment(balance, annual_interest_rate):
    current_balance = balance
    monthly_interest_rate = annual_interest_rate / 12
    low_payment = current_balance / 12
    high_payment = current_balance * (1 + monthly_interest_rate) ** 12 / 12
    while True:
        current_balance = balance
        fixed_payment = (high_payment + low_payment) / 2
        for month in range(12):
            unpaid_balance = current_balance - fixed_payment
            current_balance = unpaid_balance * (1 + monthly_interest_rate)
        if high_payment - low_payment <= 0.01:
            break
        elif current_balance > 0.0:
            low_payment = fixed_payment
            continue
        elif current_balance < 0.0:
            high_payment = fixed_payment
            continue
        else:
            break
    return round(fixed_payment, 2)


if __name__ == "__main__":
    balance = 999999
    annual_interest_rate = 0.18
    print("Lowest payment:", fixed_monthly_payment(balance, annual_interest_rate))
