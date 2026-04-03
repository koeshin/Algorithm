import sys


N=int(sys.stdin.readline())

plus=[]
minus=[]
for i in range(N):
    tmp=int(sys.stdin.readline())

    if tmp<=0:
        minus.append(tmp)
    else:
        plus.append(tmp)
minus=sorted(minus)
plus=sorted(plus,reverse=True)



    
res=0
cur=None
for i in range(len(plus)):
    a=plus[i]
    if cur is None:
        cur=a
    else:
        
        c=cur*a
        
        if c>a+cur:
            res+=c
        else:
            res+=a+cur
        cur=None
if cur is not None:
    res+=cur
    cur=None
    
for i in range(len(minus)):
    a=minus[i]
    if cur is None:
        cur=a
    else:
        
        c=cur*a
        
        if c>a+cur:
            res+=c
        else:
            res+=a+cur
        cur=None
if cur is not None:
    res+=cur
    cur=None


print(res)