for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    l=[]
    for i in a:
        if(i==1):
            count+=1
        else:
            count-=1
        l.append(count)
    if -1 in l:
        print("Invalid")
    else:
        print("Valid")
