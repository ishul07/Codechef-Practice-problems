for i in range(int(input())):
    n=int(input())
    l=[]
    p=[]
    q=[]
    r=[]
    for j in range(n):
        first,name=input().split()
        full=first+" "+name
        l.append(first)
        q.append(full)
    for j in range(n):
        for k in range(j+1,n):
            if(l[j]==l[k]):
              p.append(j)
              p.append(k)
    for j in range(n):
        if j in p:
          r.append(q[j])
        else:
            r.append(l[j])
    for j in r:
        print(j)

                   
    
