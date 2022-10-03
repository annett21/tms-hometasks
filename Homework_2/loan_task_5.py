loan = int(input("All amount of your loan: "))
percent = (float(input("Your loan percents: "))) / 100
years = int(input("Now many years you will pay for loan: "))

if percent <= 0:
    print("Loan percents must be greater then 0!")
else:
    month_payment = (loan * percent * ((1 + percent) ** years)) / (
        12 * ((1 + percent) ** years - 1)
    )
    total_pay = month_payment * 12 * years
    print("Every month you need to pay:", month_payment)
    print(f"For {years} years you'll pay:", total_pay)
    print(
        f"With {percent * 100} % for {years} years you'll overpay:",
        total_pay - loan,
    )
