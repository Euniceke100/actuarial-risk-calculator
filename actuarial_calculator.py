# Actuarial Risk Calculator
# Created by Eunice Mueni

def future_value(principal, rate, years):
    return principal * (1 + rate) ** years


def present_value(amount, rate, years):
    return amount / ((1 + rate) ** years)


def annuity_value(payment, rate, years):
    return payment * (((1 + rate) ** years - 1) / rate)


print("ACTUARIAL RISK CALCULATOR")
print("-------------------------")

print("1. Future Value")
print("2. Present Value")
print("3. Annuity Value")

choice = input("Choose calculation (1/2/3): ")

amount = float(input("Enter amount: "))
rate = float(input("Enter interest rate (example 0.05): "))
years = int(input("Enter number of years: "))

if choice == "1":
    result = future_value(amount, rate, years)
    print("Future Value:", round(result, 2))

elif choice == "2":
    result = present_value(amount, rate, years)
    print("Present Value:", round(result, 2))

elif choice == "3":
    result = annuity_value(amount, rate, years)
    print("Annuity Value:", round(result, 2))

else:
    print("Invalid choice")
