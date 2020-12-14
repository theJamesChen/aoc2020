## DAY 13
file = "d13.txt"
with open(file) as f:
    data = f.read().rstrip()

splitdata = data.split('\n')
schedules = [int(i) for i in splitdata[1].split(',') if i != 'x']
og_schedules = [int(i) if i != 'x' else i for i in splitdata[1].split(',')]
times = [-1 * splitdata[1].split(',').index(str(x)) for x in schedules]
print(og_schedules)
print(schedules)
print(times)
times_neg = [i*-1 for i in times]
print(times_neg)


from functools import reduce
def remainder_theorem(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

print(remainder_theorem(schedules, times))
