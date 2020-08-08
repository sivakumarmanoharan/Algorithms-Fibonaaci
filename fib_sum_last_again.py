a=[0,1]
b=[]
m,n=map(int,input().split())
if n==0:
    print(a[0])
elif n==1:
    print(a[1])
else:
    for i in range(2,n+1):
        fib=a[i-1]+a[i-2]
        a.append(fib)
    b=a[m:n+1]
    print(sum(b)%10)
