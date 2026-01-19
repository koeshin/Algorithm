import sys
import math

N=int(sys.stdin.readline())
dp=list(map(int,sys.stdin.readline().strip().split()))
dp.insert(0,0)


for i in range(1,N+1):
    
    if i==1:
        continue
    elif i==2:
        dp[i]=max(dp[i-1]*2,dp[i])
    else:        
        k=math.floor(i//2)
        for j in range(1,k+1):
            dp[i]=max(dp[i],dp[i-j]+dp[j])

print(dp[N])