import sys


N=int(sys.stdin.readline())


graph=[]
visited=[[False]*N for _ in range(N)]

global res

res=[]


for i in range(N):
    tmp=sys.stdin.readline().strip()

    graph.append(tmp)
    

direction=[(0,1),(0,-1),(1,0),(-1,0)]

def find_land():
    start=None
    for i in range(N):
        for j in range(N):
            if int(graph[i][j])==1 and visited[i][j] is False:
                start=(i,j)
                return start
    return start

def bfs(start):
    global res
    cnt=1
    qq=[start]
    visited[start[0]][start[1]]=True
    while(qq):
        x,y=qq.pop(0)
        
        for dx,dy in direction:
            m_y=dy+y
            m_x=dx+x

            # print(m_y,m_x)
            if 0<=m_x<N and 0<=m_y<N:
                # if m_y==1 and m_x==4:
                    # print(graph[m_x][m_y])
                    # print(visited[m_x][m_y])
                if int(graph[m_x][m_y])==1 and visited[m_x][m_y]is False:
                    qq.append((m_x,m_y))
                    visited[m_x][m_y]=True
                    cnt+=1
    res.append(cnt)
    return

def sol():
    
    while(True):
        start=find_land()
        # print(start)
        if start is None:
            break
        bfs(start)
        # print(visited)

sol()
# bfs((0,4))

print(len(res))

res=sorted(res)

for r in res:
    print(r)
    
    

    
        
    

