# Actuarial Risk Calculator
# Created by Eunice Mueni

def future_value(principal, rate, years):
    return principal * (1 + rate) ** years


def present_value(amount, rate, years):
    return amount / ((1 + rate) ** years)


def annuity_value(payment, rate, years):
    return payment * (((1 + rate) ** years - 1) / rate)


print("Actuarial Risk Calculator")

investment = float(input("Enter investment amount: "))
interest_rate = float(input("Enter annual interest rate (example 0.05): "))
years = int(input("Enter number of years: "))

print("\nFuture Value:")
print(future_value(investment, interest_rate, years))

print("\nPresent Value:")
print(present_value(investment, interest_rate, years))

payment = float(input("\nEnter yearly payment for annuity: "))

print("\nAnnuity Value:")
print(annuity_value(payment, interest_rate, years))
