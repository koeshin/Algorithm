import sys

N= int(sys.stdin.readline())

def sol(N):
    dp=[0]*(N//2+1)

    if N%2!= 0:
        return 0

    else:
        dp[1]=3
        
        for i in range(2,N//2+1):
            if i==1: 
                dp[i]=dp[i-1]*3+2
            else:
                dp[i]=dp[i-1]*3+2
                
                for j in range(i-2,0,-1):
                    dp[i]+=dp[j]*2
                    

    
    return dp[N//2]

print(sol(N))
