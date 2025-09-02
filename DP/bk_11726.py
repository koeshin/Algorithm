
x=int(input())

def solution(x):
    check=[0]*1001
    
    # 기저 확인
    check[1]=1  # n이 1일 경우
    check[2]=2  # n이 2일 경우
    
    
    for i in range(3,x+1):
        check[i]=(check[i-1]+check[i-2])%10007
    
    return check[x]

print(solution(x))