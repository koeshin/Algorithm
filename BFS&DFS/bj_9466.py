import sys
sys.setrecursionlimit(10**6)

T=int(sys.stdin.readline())

def dfs(start):
    print('start:',start)
    global total
    
    if visited[start] ==1: #방문하지 않았을 경우
        visited[start]=0
        dfs(choose[start-1])
    elif done[start] == 1:
        
        tmp=0
        
        nxt=choose[start-1]
        while nxt!= start:
            nxt=choose[nxt-1]
            print('cur:',nxt)
            tmp+=1
        
        total-=tmp
        done[start]=0
    return 

for _ in range(T):
    n=int(sys.stdin.readline())
    choose=list(map(int,sys.stdin.readline().split()))
    global visited
    visited=[1]*(n+1)
    done=[1]*(n+1)
    global total
    total=n
    for i in  range(1,n+1):
        
        if visited[i] == 1:
            visited[i]=0
            dfs(choose[i-1])


    print(total)
        
