for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    co=0
    for j in range(n):
        if(a[j]>=a[k-1]):
            co+=1
    print(co)
    
    
