def pisanoPeriod(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current= current, (previous + current) % m

        if (previous == 0 and current == 1):
            return i + 1
a=[0,1]
n,m=map(int,input().split())
if n==0:
    print(a[0])
elif n==1:
    print(a[1])
else:
    pis_period=pisanoPeriod(m)
    n=n%pis_period
    for i in range(2,n+1):
        fib=(a[i-1]+a[i-2])%m
        a.append(fib)
    print(a[n])
