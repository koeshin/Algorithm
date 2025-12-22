import sys


DEFAULT=100

N=int(sys.stdin.readline())
numbers=[i for i in range(10)]

brokens=int(sys.stdin.readline())

bro_nums=list(map(int,sys.stdin.readline().split()))

for _ in range(brokens):
    numbers.remove(bro_nums[_])
    

res= abs(N-DEFAULT)

if brokens==10 :
    print(res)
    exit()



for i in range(1000001):
    btn=len(str(i))
    
    chk=True
    for n in str(i):
        if int(n) in bro_nums:
            chk=False
            break
    
    if chk is True:
        res=min(res,abs(N-i)+btn)
    

print(res)