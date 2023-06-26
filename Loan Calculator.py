import math
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument("--type") #, choices=['diff', 'annuity']
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
 
args = parser.parse_args()
t = args.type
p = args.principal
a = args.payment
n = args.periods
i = args.interest
 
all_args = [t, p, a, n, i]
if any([x is not None and x < 0 for x in all_args[1:]]):
    print('Incorrect parameters.')
    exit()
 
if i is not None:
    i /= 1200
 
if t == 'annuity':
    if p is None and None not in [a, n, i]:
        p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        print(f'Your loan principal = {int(p)}!')
    elif a is None and None not in [p, n, i]:
        a = p * ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        print(f'Your annuity payment = {math.ceil(a)}!')
        print(f'Overpayment = {round(math.ceil(a) * n - p)}')
    elif n is None and None not in [a, p, i]:
        n = math.ceil(math.log(a / (a - i * p), 1 + i))
        if n < 12:
            print(f'It will take {n} month{"s" if n > 1 else ""} to repay the loan!')
        elif n % 12 == 0:
            print(f'It will take {n // 12} {"s" if n // 12 > 1 else ""} to repay the loan!')
        else:
            print(f'It swill take {n // 12} year{"s" if n // 12 > 1 else ""} and {n - 12 * (n // 12)} month{"s" if n > 1 else ""} to repay the loan!')
        print(f'Overpayment = {round(math.ceil(a) * n - p)}')
    else:
        print('Incorrect parameters.')
elif t == 'diff':
        if a is None and None not in [p, n, i]:
            overpayment = 0
            for m in range(1, n+1):
                d = p / n + i * (p - (p * (m - 1) / n))
                print(f'Month {m}: payment is {math.ceil(d)}')
                overpayment += math.ceil(d)
            print(f'\nOverpayment = {overpayment - int(p)}')
        else:
            print('Incorrect parameters.')
else:
    print('Incorrect parameters.')
