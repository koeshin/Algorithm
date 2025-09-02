import sys


sys.setrecursionlimit(10**7)  # 깊은 재귀 대비
x=int(sys.stdin.readline())



dp=[0]*(x+1)
def fun1(num):

    if num==1 :
        return 0

    if dp[num]!=0:
        return dp[num]
    
    res= fun1(num-1) +1 
    
    if num%3==0:
        res= min(res,fun1(num//3)+1)
    if num%2==0:
        res=min(res,fun1(num//2)+1)
    
    dp[num]=res
    
    return res
    
fun1(x)
print(dp[x])