def lcmcomp(x,y):
    return int((x*y)/gcdcomp(x,y))
def gcdcomp(m,n):
    if n==0:
        return m
    else:
        x=m%n
        return gcdcomp(n,x)
n,m=map(int,input().split())
print(lcmcomp(n,m))
