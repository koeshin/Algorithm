import sys


input=sys.stdin.readline().strip()
print(input)
idx=0
res=''
middle=0

for i in range(len(input)-1,-1,-1):
    t_pow=idx%3
    tmp=int(input[i])
    middle+=(2**t_pow)*tmp

    
    if t_pow==2 or i==0:
        res+=str(middle)
        middle=0
    idx+=1
print(res[::-1])