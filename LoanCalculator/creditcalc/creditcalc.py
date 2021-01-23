import math
import argparse
import sys

parser = argparse.ArgumentParser()  # object to hold argument information
parser.add_argument("--type")
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
args = parser.parse_args()  # returns data from the option specified
gu = sys.argv

def start():
    valid_choice = ["diff", "annuity"]
    if args.interest == None:
        print("Incorrect parameters")
    try:
        if args.type in valid_choice:
            if args.type == "diff":
                if not args.payment:
                    differentiated_payments(args.principal, args.periods, args.interest)
            elif args.type == "annuity":
                if not args.periods:
                    number_of_monthly_payments(args.principal, args.payment, args.interest)
                elif not args.principal:
                    loan_principal(args.payment, args.periods, args.interest)
                elif not args.payment:
                    annuity_monthly_payment_amount(args.principal, args.periods, args.interest)
    except:
        print("Incorrect parameters")


def differentiated_payments(loan_principal_amount, number_of_months, loan_interest):
    total_pay = 0
    for i in range(1, number_of_months + 1):
        nominal_interest = (loan_interest / 100) / 12
        payment_amount = (loan_principal_amount / number_of_months) + (
                nominal_interest * (loan_principal_amount - ((loan_principal_amount * (i - 1)) / number_of_months)))

        total_pay += math.ceil(payment_amount)
        print(f"Month {i}: payment is {math.ceil(payment_amount)}")
    total_pay -= loan_principal_amount
    print(f"Overpayment = {total_pay}")


def number_of_monthly_payments(loan_principal_amount, monthly_payment, loan_interest):
    nominal_interest = (loan_interest / 100) / 12
    number_of_months = math.log(monthly_payment / (monthly_payment - nominal_interest * loan_principal_amount),
                                (1 + nominal_interest))
    number_of_months = math.ceil(number_of_months)
    years = number_of_months // 12
    month = number_of_months % 12
    if number_of_months == 1:
        print(f'It will take {number_of_months} month to repay this loan!')
    elif number_of_months < 13:
        print(f'It will take {number_of_months} months to repay this loan!')
    elif number_of_months >= 14:
        if number_of_months % 12 == 0:
            print(f'It will takes {years} years to repay this loan!')
        else:
            print(f'It will take {years} years and {month} months to repay this loan!')
    overpayment = 0
    for i in range(1, number_of_months + 1):
        overpayment += monthly_payment
    overpayment -= loan_principal_amount
    print(f'Overpayment = {overpayment}')


def annuity_monthly_payment_amount(loan_principal_amount, number_of_periods, loan_interest):
    nominal_interest = (loan_interest / 100) / 12
    annuity_payment = loan_principal_amount * \
                      ((nominal_interest * math.pow((1 + nominal_interest), number_of_periods))
                       / (math.pow((1 + nominal_interest), number_of_periods) - 1))
    print(f'Your monthly payment = {math.ceil(annuity_payment)}!')


def loan_principal(annuity_payment, number_of_periods, loan_interest):
    nominal_interest = (loan_interest / 100) / 12
    principal = annuity_payment / ((nominal_interest * math.pow((1 + nominal_interest), number_of_periods) /
                                    (math.pow((1 + nominal_interest), number_of_periods) - 1)))
    print(f'Your loan principal = {principal}!')


start()
