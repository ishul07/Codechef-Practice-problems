for a in range(int(input())):
    m,n=map(int,input().split())
    rx,ry=map(int,input().split())
    s=int(input())
    c,d=0,0
    p=input()
    for i in p:
        if(i=='L'):
            c=c-1
        elif(i=='R'):
            c+=1
        elif(i=='U'):
            d+=1
        else:
            d-=1
    if(c==rx and d==ry):
        print("Case " +str(a+1)+": REACHED")
    elif(c<0 or c>m or d<0 or d>n):
        print("Case " +str(a+1)+": DANGER")
    else:
        print("Case "+str(a+1)+": SOMEWHERE")
        
