import sys

gp=[]

N,M=map(int,sys.stdin.readline().split())

for i in range(N):
    tmp=sys.stdin.readline().strip()
    tmp_list=[]
    for j in range(M):
        tmp_list.append(int(tmp[j]))
    gp.append(tmp_list)

visited=[]
for _ in range(N):
    tmp=[False]*M
    visited.append(tmp)



def bfs(gp,visited):
    
    bfs_list=[[0,0]]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    
    visited[0][0]=True
  
    while (True):
        x,y=bfs_list.pop(0)

        if (x,y)==(N-1,M-1):
            return gp[N-1][M-1]
        
        
        for i in range (4):
            tx=x+dx[i]
            ty=y+dy[i]
        

            if N>tx>=0 and M>ty>=0:
              
                if gp[tx][ty]!=0 and visited[tx][ty] is False:
                  
                    gp[tx][ty]=gp[x][y]+1
                    visited[tx][ty]=True
                    bfs_list.append([tx,ty])
     
        return -1
        
print(bfs(gp,visited)) 
    
    
    
    