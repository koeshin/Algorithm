import sys

n=int(sys.stdin.readline())


dict={}


t=list(map(int,sys.stdin.readline().split()))
def sol(t):
    a=max(t)
    if a==0:
        print(0)
        return
    points=[0]*(a+1)
    

    for num in t:
        points[num]+=num
        
    dp=[0]*(a+1)
    dp[1]=points[1]

    
    for i in range(2,a+1):
        
        dp[i]=max(dp[i-1],dp[i-2]+points[i])

    print(dp[a])
    return

sol(t)