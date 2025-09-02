import sys


ctxt=sys.stdin.readline().strip()

dp=[1]*(len(ctxt)+1)



for i in range(1,len(ctxt)):
    
    front=int(ctxt[i-1])
    now=int(ctxt[i])

    
    if front == 1:

        dp[i+1]= dp[i]+dp[i-1]
        
    elif front ==2:
        if 1<= now < 7:

            dp[i+1]=dp[i]+dp[i-1]
    else:
        dp[i+1]=dp[i-1]


print(dp[len(ctxt)]%1000000)