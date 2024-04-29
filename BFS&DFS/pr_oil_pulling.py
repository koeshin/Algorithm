from collections import deque




def BFS(maps,start,visited):
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue=deque()
    queue.append(start)
    oils=1
    if visited[start[0]][start[1]]==True:
        return 0
    end=None
    
    while queue:
        now=queue.popleft()
        x,y=now
        visited[x][y]=True
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            
            if 0<= cx < len(maps) and 0<= cy < len(maps[0]):
                if visited[cx][cy]==False and maps[cx][cy]==1:
                    visited[cx][cy]=True
                    queue.append((cx,cy))
                    # end=(cx,cy)
                    oils+=1
                    
    
    return oils

############# 시간 초과 코드 ##########
def solution(land):
    colums=len(land[0])
    rows=len(land)
    
    MAX=0
    for colum in range(colums):
        results=[]
        starts=[]
        visited=[[False]*colums for _ in range(rows)]
        tmp_land=land.copy()
        for row in range(rows):
            if land[row][colum]==1:
                starts.append((row,colum))
        # print("starts:",starts)      
        for start in starts:
            
            result=BFS(tmp_land,start,visited)
            results.append(result)
        if sum(results)>MAX:
            MAX=sum(results)
    
    return MAX
# land=[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
# print(solution(land))
                    
######################## 정답 코드#####################


def BFS2(maps,start,visited):
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue=deque()
    queue.append(start)
    oils=1
    min_y=1000
    max_y=0

    
    while queue:
        now=queue.popleft()
        x,y=now
        min_y=min(min_y,y)   # 석유가 들어있는 최소 컬럼 값 
        max_y=max(max_y,y)   # 석유가 들어있는 최대 컬럼값
        visited[x][y]=True
        for i in range(4):
            cx=x+dx[i]
            cy=y+dy[i]
            
            if 0<= cx < len(maps) and 0<= cy < len(maps[0]):
                if visited[cx][cy]==False and maps[cx][cy]==1: # map[x][y]!=0 보다는 ==1이 더 효율적인 방법
                    visited[cx][cy]=True
                    queue.append((cx,cy))
                    # end=(cx,cy)
                    oils+=1
                    
    
    return oils,min_y,max_y

def solution2(land):   
    colums=len(land[0])
    rows=len(land)
    result=[0]*colums   # 컬럼마다 시추한 석유 양을 담을 리스트
    visited=[[False]*colums for i in range(rows)] 
    for i in range(colums):
        for j in range(rows):
            if land[j][i]==1 and visited[j][i]==False:   # 석유가 있고 방문하지 않았을 경우만 BFS
                oils,min_y,max_y=BFS2(land,(j,i),visited)
               
                for idx in range(min_y,max_y+1):   # 컬러마다 시추한 석유양 더해주기
                    result[idx]+=oils

     


    
    return max(result)
land=[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 0], [1, 1, 1, 1]]

land=[[1, 1, 1, 1, 0],
[1, 0, 0, 0, 0],
[0, 0, 0, 1, 1],
[1, 0, 0, 1, 0],
[1, 1, 0, 1, 0]]
print(solution2(land))
