import sys
from collections import deque 


N,M=list(map(int,(sys.stdin.readline().split())))
graph=[]
for i in range(M):
    tmp=list(map(int,(sys.stdin.readline().split())))
    graph.append(tmp)
    


cnt_graph=[[0]*N for _ in range(M) ]

dx=[1,-1,0,0]
dy=[0,0,1,-1]



start=deque()
for i in range(len(graph)):
    for j in range(len(graph[i])) :
        if graph[i][j]==1:
            start.append([i,j])

def bfs(V):
    
    queue=V
    while(queue):
        start=queue.popleft()
        x=start[0]
        y=start[1]


        for j in range(len(dx)):
            tmp_x=x+dx[j]
            tmp_y=y+dy[j]
            
            if 0<=tmp_x<M and 0<=tmp_y<N:
                if graph[tmp_x][tmp_y]==0:
                    queue.append([tmp_x,tmp_y])
                    graph[tmp_x][tmp_y]=graph[x][y]+1


bfs(start)
# print(visited)        
flag=1
max=0
for i in range(len(graph)):
    if flag==-1:
        break
    for j in range(len(graph[i])):
        if graph[i][j]==0 :
            print(-1)
            exit(0)
        else:
            if graph[i][j] >max:
                max=graph[i][j]


print(max-1)


    