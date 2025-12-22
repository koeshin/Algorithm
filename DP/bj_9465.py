import sys


T=int(sys.stdin.readline())



def sol(n,stiker):
    dp=[[0]*n for _ in range(2)]
    
    dp[0][0]=stiker[0][0]
    dp[1][0]=stiker[1][0]
    
    if n==1:
        res=max(dp[0][0],dp[1][0])
        return res ## 주의 이것때문에 98%에서 인덱스 에러남
    dp[0][1]=dp[1][0]+stiker[0][1]
    dp[1][1]=dp[0][0]+stiker[1][1]
    if n==2:
        res=max(dp[0][1],dp[1][1])
        return res
    else:
        for i in range(2,n):
            dp[0][i]=stiker[0][i]+max(dp[1][i-1],dp[1][i-2]) 
            dp[1][i]=stiker[1][i]+max(dp[0][i-1],dp[0][i-2])
        res=max(dp[0][-1],dp[1][-1])
    
        return res

for _ in range(T):
    n=int(sys.stdin.readline())
    stiker=[]
    for __ in range(2):
        tmp=list(map(int,sys.stdin.readline().split()))
        stiker.append(tmp)
    rs=sol(n,stiker)
    print(rs)