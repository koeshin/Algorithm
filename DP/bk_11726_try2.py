
import sys
input=int(sys.stdin.readline().strip())

global ans
ans=[0]*(input+1)
def solution(n):
    # print(n)
    ans[1]=1
    ans[2]=2
    if ans[n]!=0:
        return ans[n]
    
    ans[n]=solution(n-1)+solution(n-2)
    return ans[n]

print(solution(input)%10007)