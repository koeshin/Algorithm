import sys


N= int(sys.stdin.readline())


dp=[0]*(N+1)

steps=[0]

for i in range(N):
    
    tmp=int(sys.stdin.readline())
    steps.append(tmp)


def solution(N,dp,steps):
    
    for i in range(1,N+1):
        if i <3:
            dp[i]=steps[i]+dp[i-1]
        else:
            
            dp[i]=max(dp[i-3]+steps[i-1],dp[i-2])+steps[i]
    

    return dp[N]


print(solution(N,dp,steps))

