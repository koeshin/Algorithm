import sys
from collections import deque

grid=[]

N=int(sys.stdin.readline().strip())
for _ in range(N):
    tmp=list(map(int,sys.stdin.readline().split()))
    grid.append(tmp)



'''def make_label(grid):
    borders=[]
    land_cnt=10000
    for i in range(N):
        for j in range(N):
            if grid[i][j]==1:
                border=check_island((i,j),land_cnt)
                borders.append(border)
                land_cnt+=1

    # for _ in range(N):
    #     print(grid[_])

    return grid,borders



def check_island(point,land_cnt):
    
    move=[(1,0),(-1,0),(0,1),(0,-1)]
    qq=deque([point])
    border=[]

    while(qq):
        a,b=qq.popleft()
        grid[a][b]=land_cnt
        is_border=False

        for dx,dy in move:

            t_a=a+dx
            t_b=b+dy
            if 0<=t_a<N and 0<=t_b<N: 
                if grid[t_a][t_b]==1:
                    qq.append((t_a,t_b))
                elif grid[t_a][t_b]==0:
               
                    is_border=True
            
        if is_border is True:
            border.append((a,b))
   

    return border
            

def find_brige(grid,borders):
    
    
    min_bridge=10**8
    move=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(len(borders)-1):
        visited=[[False]*N for _ in range(N)]

        copy_grid = [row[:] for row in grid]  # 깊은 복사 ->  메모리 초과 발생
        
        border=deque(borders[i])
        
        tmp_x,tmp_y=border[0]
        now_land=copy_grid[tmp_x][tmp_y]
        while(border):
            x,y=border.popleft()
            for dx,dy in move:
                m_x=x+dx
                m_y=y+dy
                
                if  0<=m_x<N and 0<=m_y<N:
                    if copy_grid[m_x][m_y]==0 and visited[m_x][m_y] is False:
                        copy_grid[m_x][m_y]+=copy_grid[x][y]-1
                        visited[m_x][m_y]=True
                        border.append((m_x,m_y))
                    elif copy_grid[m_x][m_y]> now_land:
                        min_bridge=min(min_bridge,now_land-copy_grid[x][y])
        # print('copy_Grid')
        # for _ in range(N):
        #     print(copy_grid[_])
    return min_bridge
                    
    

grid,borders=make_label(grid)
res=find_brige(grid,borders)

print(res)'''


# 1. 섬 라벨링
label = [[0]*N for _ in range(N)]
island_id = 0
moves = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs_label(sx, sy, island_id):
    q = deque()
    q.append((sx, sy))
    label[sx][sy] = island_id

    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] == 1 and label[nx][ny] == 0:
                    label[nx][ny] = island_id
                    q.append((nx, ny))

for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and label[i][j] == 0:
            island_id += 1
            bfs_label(i, j, island_id)

# 2. 멀티 소스 BFS로 최단 다리 찾기
dist = [[-1]*N for _ in range(N)]
q = deque()

# 모든 섬의 땅을 BFS 시작점으로 넣기
for i in range(N):
    for j in range(N):
        if label[i][j] != 0:
            dist[i][j] = 0
            q.append((i, j))

ans = 10**9

while q:
    x, y = q.popleft()
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N:
            # 아직 아무 섬에도 안 속한 바다인 경우: 확장
            if label[nx][ny] == 0:
                label[nx][ny] = label[x][y]      # 어느 섬에서 왔는지 표시
                dist[nx][ny] = dist[x][y] + 1    # 거리 1 증가
                q.append((nx, ny))
            # 다른 섬에서 온 파동과 만난 경우: 다리 길이 계산
            elif label[nx][ny] != label[x][y]:
                # 두 섬에서 온 거리 합이 다리 길이
                ans = min(ans, dist[nx][ny] + dist[x][y])

print(ans)
