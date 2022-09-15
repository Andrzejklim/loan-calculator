import math
import argparse

parser = argparse.ArgumentParser(description='Loan calculator')
parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--principal')  # the loan principal
parser.add_argument('--periods')  # in months
parser.add_argument('--interest')  # nominal interest rate
parser.add_argument('--payment')  # monthly payment amount
args = parser.parse_args()
if args.type != "annuity":
    if args.type != "diff" or args.type == "":
        print('Incorrect parameters')


def n_of_m_payments():  # theoretically passed :D
    p = int(args.principal)
    a = int(args.payment)  # annuity/monthly payment
    i = float(args.interest)
    i = (i / (12 * 100))
    n_of_payments = math.log(a / (a - i * p), 1 + i)
    n_of_payments = math.ceil(n_of_payments)
    year = n_of_payments // 12
    month = n_of_payments % 12
    total_cost = n_of_payments * a
    overpayment = total_cost - p
    if year < 1:
        if month < 2:
            print(f'It will take {month} month to repay this loan!')
        else:
            print(f'It will take {month} months to repay this loan!')
    elif year == 1:
        if month < 1:
            print(f'It will take {year} year to repay this loan!')
        elif month < 2:
            print(f'It will take {year} year and {month} month to repay this loan!')
        else:
            print(f'It will take {year} year and {month} months to repay this loan!')
    else:
        if month < 1:
            print(f'It will take {year} years to repay this loan!')
        elif month < 2:
            print(f'It will take {year} years and {month} month to repay this loan!')
        else:
            print(f'It will take {year} years and {month} months to repay this loan!')
    print(f'Overpayment = {overpayment}')


def annuity_payment():  # theoretically passed
    p = int(args.principal)
    n = int(args.periods)
    i = float(args.interest)
    i = (i / (12 * 100))
    annuity_m_payment = p * (i * math.pow((1 + i), n) / (math.pow((1 + i), n) - 1))
    print(f'Your monthly payment = {math.ceil(annuity_m_payment)}!')
    total_cost = n * math.ceil(annuity_m_payment)
    overpayment = total_cost - p
    print(f'Overpayment = {overpayment}')


def loan_principal():  # theoretically passed
    a = float(args.payment)
    n = int(args.periods)
    i = float(args.interest)
    i = (i / (12 * 100))
    l_principal = a / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
    print(f'Your loan principal = {math.floor(l_principal)}!')
    total_cost = n * a
    overpayment = total_cost - l_principal
    print(f'Overpayment = {math.ceil(overpayment)}')


def differentiated_payments():
    p = int(args.principal)  # 1000000
    i = float(args.interest)  # 10
    n = int(args.periods)  # 10
    i = (i / (12 * 100))
    m = 1  # months
    total_cost = 0
    for _ in range(0, n):
        diff_payment_month = math.ceil((p / n) + i * (p - (p * (m - 1) / n)))
        total_cost += diff_payment_month
        print(f"Month: {m}: payment is {diff_payment_month}")
        m = m + 1
    overpayment = total_cost - p
    print(f'Overpayment = {overpayment}')


if args.type == "annuity":
    if args.principal is None and args.periods is not None and args.payment is not None and args.interest is not None:
        if float(args.periods) < 1 or float(args.payment) < 1 or float(args.interest) < 1:
            print('Incorrect parameters')
        else:
            loan_principal()
    elif args.periods is None and args.principal is not None and args.interest is not None and args.payment is not None:
        if float(args.principal) < 1 or float(args.payment) < 1 or float(args.interest) < 1:
            print('Incorrect parameters')
        else:
            n_of_m_payments()
    elif args.payment is None and args.interest is not None and args.principal is not None and args.periods is not None:
        if float(args.principal) < 1 or float(args.periods) < 1 or float(args.interest) < 1:
            print('Incorrect parameters')
        else:
            annuity_payment()
    else:
        print('Incorrect parameters')

if args.type == "diff":
    if args.principal is not None and args.interest is not None and args.periods is not None:
        if float(args.principal) < 0 or float(args.interest) < 0 or float(args.periods) < 0:
            print('Incorrect parameters')
        else:
            differentiated_payments()
    else:
        print('Incorrect parameters')
