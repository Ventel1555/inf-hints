def f(x,a):
    return x%a==0 or ((170<x<221) <= x%24!=0)
for a in range(1,10000000):
    if all(f(x,a) for x in range(1,10000000)):
        print(a)

