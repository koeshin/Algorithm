import sys


N,M,V=list(map(int,sys.stdin.readline().split()))

graph = [[0] * (N+1) for _ in range(N+1)]


for i in range(M):
    a,b=list(map(int,sys.stdin.readline().split()))
    
    graph[a][b]=1
    graph[b][a]=1

dfs_sol=[]
visited=[False]*(N+1)

def dfs(v,sol):
    
    visited[v]=True
    
    sol.append(v)
    for i in range(N+1):
        if graph[v][i]==1 and visited[i] is False:
            dfs(i,sol)


dfs(V,dfs_sol)

visited=[False]*(N+1)
def bfs(v):
    
    visited[v]=True
    
    sol=[]
    sol.append(v)
    
    qq=[v]
    
    while(qq):
        tmp=qq.pop(0)
        
        for i in range(N+1):
            if graph[tmp][i]==1 and visited[i] is False:
                visited[i]=True
                qq.append(i)
                sol.append(i)
    
    return sol

bfs_sol=bfs(V)

for i in range(len(dfs_sol)):
    print(dfs_sol[i], end=" ")

print()
for i in range(len(bfs_sol)):
    print(bfs_sol[i], end=" ")