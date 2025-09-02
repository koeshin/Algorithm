x=int(input())
dp={1:0} 
def rec(n):  # TopDown solution
    print(dp)
    if n in dp.keys():
        return dp[n]
    if (n%3==0) and (n%2==0):
        dp[n]=min(rec(n//3)+1, rec(n//2)+1)
    elif n%3==0:
        dp[n]=min(rec(n//3)+1, rec(n-1)+1)
    elif n%2==0:
        dp[n]=min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n]=rec(n-1)+1
    print(dp)
    return dp[n]
print(rec(x))


def solution(x):  # BottomUp solution
    
    tmp=[0]*(x+1)
    # 기저는 1일 때
    for i in range(2,x+1):  # 2 부터 x까지
        tmp[i]=tmp[i-1]+1   # -1은 무조건 진행. i-1값 +1
        
        if i%2==0:          # 2로 나눠지는 경우, 1을 뺸 값과 2로 나눈 값 중 작은 값
            tmp[i]=min(tmp[i//2]+1,tmp[i])
        if i%3==0:
            tmp[i]=min(tmp[i//3]+1,tmp[i])  # 현재 값과 3으로 나누 값 중 작은 수 선택
            
    return tmp[x]

print(solution(x))