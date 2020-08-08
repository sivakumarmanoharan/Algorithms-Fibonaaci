def gcdcomp(m,n):
    if n==0:
        return m
    else:
        x=m%n
        return gcdcomp(n,x)
n,m=map(int,input().split())
gcd=gcdcomp(m,n)
print(gcd)
