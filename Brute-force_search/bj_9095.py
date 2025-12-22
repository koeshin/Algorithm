import sys

T=int(sys.stdin.readline())
nums=[]

for _ in range(T):
    tmp=int(sys.stdin.readline())
    nums.append(tmp)




def minus(ans,num):
    
    
    for i in range(1,4):
        tmp=num-i
    
        if tmp>0:
            ans=minus(ans,num-i)
        elif tmp==0:
            ans+=1
            break
    return ans
    
for n in nums:
    ans=0
    
    ans=minus(ans,n)

    print(ans)
        