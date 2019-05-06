for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=sum([j**2 for j in a])
    c=a.count(1)
    if(b<=sum(a)):
        print("YES")
    else:
        if(n-c>k):
            print("NO")
        else:
            print("YES")
            
    
    
    
