import sys


T=int(sys.stdin.readline().strip())


cases=[]
for i in range(T):
    cases.append(int(sys.stdin.readline().strip()))
    

dp=[1,1,1,2,2]

for i in range(T):
    tmp=cases[i]
    
    if tmp<=len(dp):
        print(dp[tmp-1])
    
    else:
        while(tmp>=len(dp)):
            k=dp[len(dp)-1]+dp[len(dp)-5]
            dp.append(k)
            # print(dp)
        print(dp[tmp-1])
        
        