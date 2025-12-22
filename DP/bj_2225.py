import sys


N,K=list(map(int,sys.stdin.readline().split()))


def sol(N,K):
    
    dp=[[1]*(N+1) for i in range(K)]
    
    for i in range(1,K):
        for j in range(N+1):
            for k in range(j+1):
                dp[i][j]+=dp[i-1][k]
            dp[i][j]-=1
    return dp[K-1][N]


print(sol(N,K)%1000000000)
