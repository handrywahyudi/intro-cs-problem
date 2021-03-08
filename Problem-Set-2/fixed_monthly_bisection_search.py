# Problem Set 2
# Problem 3: https://bit.ly/2OtXsNy

def fixed_monthly_payment(balance, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12
    low_payment = balance / 12
    high_payment = balance * (1 + monthly_interest_rate) ** 12 / 12
    while True:
        current_balance = balance
        fixed_payment = (high_payment + low_payment) / 2
        for month in range(12):
            unpaid_balance = current_balance - fixed_payment
            current_balance = unpaid_balance * (1 + monthly_interest_rate)
        if high_payment - low_payment <= 0.01:
            break
        elif current_balance > 0.01:
            low_payment = fixed_payment
            continue
        elif current_balance < 0.01:
            high_payment = fixed_payment
            continue
        else:
            break
    return round(fixed_payment, 2)


if __name__ == "__main__":
    balance = 320000
    annual_interest_rate = 0.2
    print("Lowest payment:", fixed_monthly_payment(balance, annual_interest_rate))
