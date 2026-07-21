# Actuarial Risk Calculator
# Created by Eunice Mueni

def future_value(principal, rate, years):
    return principal * (1 + rate) ** years


def present_value(amount, rate, years):
    return amount / ((1 + rate) ** years)


def annuity_value(payment, rate, years):
    return payment * (((1 + rate) ** years - 1) / rate)


print("Actuarial Risk Calculator")

investment = 10000
interest_rate = 0.05
period = 10

print("\nFuture Value:")
print(future_value(investment, interest_rate, period))

print("\nPresent Value:")
print(present_value(investment, interest_rate, period))

print("\nAnnuity Value:")
print(annuity_value(1000, interest_rate, period))
