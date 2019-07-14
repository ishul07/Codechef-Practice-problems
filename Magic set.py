for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in a:
        if(i%m==0):
            c=c+1
    print(2**c-1)
            
    
