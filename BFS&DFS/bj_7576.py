import sys
from collections import deque

M,N=map(int,sys.stdin.readline().split())

gp=[]

for _ in range(N):
    tmp=list(map(int,sys.stdin.readline().strip().split()))
    gp.append(tmp)


def sol():
    
    bfs=deque()
    for i in range(N):
        for j in range(M):
            if gp[i][j]==1:
                bfs.append((i,j))
    
    dr=[(1,0),(-1,0),(0,1),(0,-1)]
    while(bfs):
        
        x,y=bfs.popleft()

        for dx,dy in dr:
            mx=x+dx
            my=y+dy
            
            if 0<=mx<N and 0<=my<M:
                if gp[mx][my]==0:
                    gp[mx][my]=gp[x][y]+1
                    bfs.append((mx,my))
    
    MAX=0
    for li in gp:
        for ele in li:
            if ele==0:
                print(-1)
                return
            else:
                if ele>MAX:
                    MAX=ele
    print(MAX-1)
   

    return

sol()
