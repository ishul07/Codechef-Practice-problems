for i in range(int(input())):
    n,x=map(int,input().split())
    s=input()
    c=[x]
    for j in s:
        if(j=='R'):
            x+=1
            c.append(x)
        else:
            x-=1
            c.append(x)
    c=set(c)
    print(len(c))
    
