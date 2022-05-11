import argparse
import math

parser = argparse.ArgumentParser(exit_on_error=False)

parser.add_argument('--type', choices=['annuity', 'diff'],
                    help='Define the type of payment')
parser.add_argument('--payment', type=float,
                    help='Insert the amount paid per month')
parser.add_argument('--principal', type=int,
                    help='Insert the principal loan amount')
parser.add_argument('--periods', type=int,
                    help='Insert the number of months the loan will be repaid in')
parser.add_argument('--interest', type=float,
                    help='Insert the monthly interest rate')

args = parser.parse_args()


if args.type is None or args.interest is None:
    print('Incorrect parameters'), exit()
elif args.type == 'diff':
    if args.payment:
        print('Incorrect parameters'), exit()
    elif args.principal is None or args.periods is None:
        print('Incorrect parameters'), exit()

arg_list = [args.type, args.interest]
check_list = [args.payment, args.principal, args.periods]
for i in check_list:
    if i:
        arg_list.append(i)


def get_process():
    global arg_list
    if args.periods not in arg_list:
        n()
    elif args.principal not in arg_list:
        p()
    elif args.payment not in arg_list:
        if args.type == 'annuity':
            a()
        else:
            d()


def n():
    global args
    principal = args.principal
    m_sum = args.payment
    interest = args.interest

    calc_i = interest / (12 * 100)
    base = m_sum / (m_sum - calc_i * principal)
    calc_n = math.ceil(math.log(base, 1 + calc_i))
    overpayment = math.ceil(m_sum * calc_n - principal)

    if calc_n <= 1:
        print('It will take 1 month to repay the loan')
    elif calc_n < 12:
        print(f'It will take {calc_n} months to repay the loan')
    else:
        years = calc_n // 12
        months = calc_n % 12
        if months > 0:
            if years == 1:
                print(f'It will take 1 year to repay this loan!')
            else:
                print(f'It will take {years} years and {months} months to repay this loan!')
        else:
            print(f'It will take {years} years to repay this loan!')

    print(f'Overpayment = {overpayment}')


def a():
    global args
    principal = args.principal
    m_sum = args.periods
    interest = args.interest

    calc_i = interest / (12 * 100)
    annuity = math.ceil(principal * ((calc_i * (1 + calc_i) ** m_sum) / ((1 + calc_i) ** m_sum - 1)))
    overpayment = math.ceil(annuity * m_sum - principal)

    print(f'Your monthly payment = {int(annuity)}!' + '\n' + f'Overpayment = {overpayment}')


def p():
    global args

    annuity = args.payment
    num_payments = args.periods
    interest = args.interest

    calc_i = interest / (12 * 100)
    calc = math.floor(annuity / ((calc_i * (1 + calc_i) ** num_payments) / ((1 + calc_i) ** num_payments - 1)))
    overpayment = math.ceil(annuity * num_payments - calc)

    print(f'Your loan principal = {calc}!' + f'Overpayment = {overpayment}')


def d():
    global args

    principal = args.principal
    interest = args.interest
    m_sum = args.periods

    calc_i = interest / (12 * 100)
    monthly_total = 0
    for m in range(1, m_sum + 1):
        monthly_pay = math.ceil((principal / m_sum) + calc_i * (principal - ((principal * (m - 1)) / m_sum)))
        monthly_total += monthly_pay
        print(f'Month {m}: payment is {int(monthly_pay)}')

    print('\n' + f'Overpayment = {monthly_total - principal}')


get_process()
