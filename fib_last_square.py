a=[0,1]
n=int(input())
if n==0:
    print(a[0])
elif n==1:
    print(a[1])
else:
    for i in range(2,n+2):
        fib=a[i-1]+a[i-2]
        a.append(fib)
    sum=a[n]*a[n+1]
    print(sum%10)
