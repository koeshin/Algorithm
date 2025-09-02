import sys

N=int(sys.stdin.readline().strip())
peo=list(map(int,sys.stdin.readline().split()))

peo.sort()

tmp=N
result=0
for i in range(len(peo)):
    result+= peo[i]*tmp
    tmp-=1
    
print(result)