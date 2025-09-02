import sys


N=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

dp=[-1000]*(N+1)
dp[0]=nums[0]


for i in range(1,N):
    dp[i]=max(dp[i-1]+nums[i],nums[i])

print(max(dp))