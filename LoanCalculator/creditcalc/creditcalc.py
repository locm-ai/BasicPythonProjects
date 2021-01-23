import math


def start():
    print('What do you want to calculate?')
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount')
    print('type "p" for loan principal:')
    user_action = input()
    if user_action == 'n':
        number_of_monthly_payments()
    elif user_action == 'a':
        annuity_monthly_payment_amount()
    elif user_action == 'p':
        loan_principal()


def number_of_monthly_payments():
    loan_principal_amount = int(input('Enter the loan principal:\n'))
    monthly_payment = int(input('Enter the monthly payment:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))
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
        print(f'It will take {years} years and {month} months to repay this loan!')


def annuity_monthly_payment_amount():
    loan_principal_amount = int(input('Enter the loan principal:\n'))
    number_of_periods = int(input('Enter the number of periods:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))
    nominal_interest = (loan_interest / 100) / 12
    annuity_payment = loan_principal_amount *\
                      ((nominal_interest * math.pow((1 + nominal_interest), number_of_periods))
                      / (math.pow((1 + nominal_interest), number_of_periods) - 1))
    print(f'Your monthly payment = {math.ceil(annuity_payment)}!')


def loan_principal():
    annuity_payment = float(input('Enter the annuity payment:\n'))
    number_of_periods = int(input('Enter the number of periods:\n'))
    loan_interest = float(input('Enter the loan interest:\n'))
    nominal_interest = (loan_interest / 100) / 12
    loan_principal = annuity_payment / ((nominal_interest * math.pow((1 + nominal_interest), number_of_periods) /
         (math.pow((1+nominal_interest), number_of_periods) - 1)))
    print(f'Your loan principal = {loan_principal}!')


start()
