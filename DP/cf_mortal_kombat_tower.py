import sys


t=int(sys.stdin.readline())


def sol(n,li):
    INF=float('inf')
    dp=[[INF,INF] for _ in range(n+1)]
    ## 0은 친구 1은 나
    dp[0][0] = 0
    
    
    for i in range(0,n):
        # 현재 친구 차례 -> 다음 내차례를 갱신 내 차례에 값을 넣기
        if dp[i][0] != INF:
            if i+1<=n:
                dp[i+1][1]=min(dp[i+1][1],dp[i][0]+li[i])
            if i+2<=n:
                dp[i+2][1]=min(dp[i+2][1],dp[i][0]+li[i]+li[i+1])

        # 현재 내 차례 -> 다음 친구 차례 갱신
        if dp[i][1] != INF:
            if i+1<=n:
                dp[i+1][0]=min(dp[i+1][0],dp[i][1])
            if i+2<=n:
                dp[i+2][0]=min(dp[i+2][0],dp[i][1])
    return(min(dp[n]))



for _ in range(t):
    n=int(sys.stdin.readline())
    li=list(map(int,sys.stdin.readline().split()))

    print(sol(n,li))