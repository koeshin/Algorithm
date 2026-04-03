import sys

N=int(sys.stdin.readline())

maps=[[] for _ in range(N+1)]

for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())

    maps[a].append(b)
    maps[b].append(a)

parents=[0]*(N+1)
def BFS(maps):
    
    bfs_list=[]
    
    for node in maps[1]:
        bfs_list.append(node)
        parents[node]=1
    
    while bfs_list:
        cur=bfs_list.pop(0)

        for node in maps[cur]:
            if node!=1 and parents[node]==0:
                parents[node]=cur
                bfs_list.append(node)
    return

BFS(maps)
for i in range(2,N+1):
    print(parents[i])

        
        
        
    
    
    