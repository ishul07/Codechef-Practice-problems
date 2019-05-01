import datetime
for i in range(int(input())):
    y,m,d=map(int,input().split(':'))
    m=datetime.datetime(y,m,d)
    count=1
    oe=d%2
    while True:
        m=m+datetime.timedelta(days=2)
        if(m.day%2!=oe):
            break
        count+=1
    print(count)
        
            
