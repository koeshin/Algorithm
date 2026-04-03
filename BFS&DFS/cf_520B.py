import sys
from collections import deque
a,b= map(int,sys.stdin.readline().split())

global find_n,g_cnt

find_n=b

def sol(n,cnt):
    
    qq=deque()
    qq.append(n)

    
    flag=True
    limit = 20000
    dist = [-1] * (limit + 1)
    
    while(flag):
       
        tmp=qq.popleft()

        if tmp==find_n:
            print(dist[tmp]+1)
            break
        for next_val in [tmp * 2, tmp - 1]:
                    # 유효 범위 내에 있고, 아직 방문하지 않은 숫자라면
                    if 0 <= next_val <= limit and dist[next_val] == -1:
                        dist[next_val] = dist[tmp] + 1
                        qq.append(next_val)
    

sol(a,0)
