import sys

round=int(sys.stdin.readline().strip())
inputs=[]
for i in range(round):
    input=(int(sys.stdin.readline().strip()))
    inputs.append(input)

def solution(n,ans):
    # bais ,1,2,3
    if ans[n]!=0:
        return ans[n]
    else:
        if n<=2:
            ans[n]=n
            return ans[n]
        elif n==3:
            ans[n]=n+1
            return ans[n]
        
        ans[n]=solution(n-1,ans)+solution(n-2,ans)+solution(n-3,ans)
        return ans[n]


for k in inputs:
    ans=[0]*(k+1)
    solution(k,ans) 
    print(solution(k,ans))