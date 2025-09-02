
x=int(input())
def solution(x):  # BottomUp solution

    tmp=[0]*(x+1)
    
    for i in range(2,x+1):
        tmp[i]=tmp[i-1]+1
        
        if i%2==0:
            tmp[i]=min(tmp[i//2]+1,tmp[i])
        if i%3==0:
            tmp[i]=min(tmp[i//3]+1,tmp[i])
    
    return tmp[x]

print(solution(x))