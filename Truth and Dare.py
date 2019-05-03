for i in range(int(input())):
    tr=int(input())
    a=set(map(int,input().split()))
    dr=int(input())
    b=set(map(int,input().split()))
    ts=int(input())
    c=set(map(int,input().split()))
    ds=int(input())
    d=set(map(int,input().split()))
    if(d.issubset(b) and c.issubset(a)):
        print("yes")
    else:
        print("no")
        
