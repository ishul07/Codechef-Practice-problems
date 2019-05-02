n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
target=0
for i in range(q):
    target=0
    l,r=map(int,input().split())
    for j in range(l-1,r):
        target+=a[j]*b[j]
    print(target)
    
