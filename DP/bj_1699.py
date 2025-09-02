import sys


N= int(sys.stdin.readline())

dp=[i for i in range(N+1)]


def sol(N):
    
    for i in range(1,N+1):
        if i==1:
            dp[i]=1
            continue

        for j in range(1,i+1):

            square=j**2    
            
            if square>i:
                break
                
            if dp[i]>dp[i-square]+1:
                dp[i]=dp[i-square]+1
                

sol(N)
print(dp[N])