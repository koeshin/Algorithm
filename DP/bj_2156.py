import sys


n=int(sys.stdin.readline())

wine=[]
dp=[0]*(n+1)
for i  in range(n):
    wine.append(int(sys.stdin.readline()))


for i in range(n):
    
    if i==0:
        dp[i+1]=wine[i]
    elif i==1:
        dp[i+1]=wine[i]+wine[i-1]
    
    else:
        dp[i+1]=max(dp[i-2]+wine[i]+wine[i-1],dp[i-1]+wine[i],dp[i])

        

print(dp[n])