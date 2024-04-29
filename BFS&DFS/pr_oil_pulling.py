from collections import deque

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
                if visited[cx][cy]==False and maps[cx][cy]!=0:
                    # maps[cx][cy]=maps[x][y]+1
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
                    
######################## 수정 중인 코드#####################
def solution2(land):   # 이  코드는 for문이 너무 많아서 시간 초과
    colums=len(land[0])
    rows=len(land)
    dict={}
    tmp_land=land.copy()
    MAX=0
    for colum in range(colums):
        print("dict",dict)
        results=[]
        starts=[]
        visited=[[False]*colums for _ in range(rows)]

        for row in range(rows):
            if land[row][colum]>=1:
                starts.append((row,colum))
        check={}    
        print("starts:",starts)  
        for start in starts:
            print("check:",check)   
            x,y=start
            if tmp_land[x][y] !=1:
                if tmp_land[x][y] not in check:
                    print(tmp_land[x][y])
                    results.append(dict[tmp_land[x][y]])
                    check[tmp_land[x][y]]=result
            else:
                result=BFS(tmp_land,start,visited)
                dict[colum+2]=result
                check[colum+2]=result
                results.append(result)
        print("results:",results)
        if sum(results)>MAX:
            MAX=sum(results)
    
    return MAX
land=[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 0], [1, 1, 1, 1]]

land=[[1, 1, 1, 1, 0],
[1, 0, 0, 0, 0],
[0, 0, 0, 1, 1],
[1, 0, 0, 1, 0],
[1, 1, 0, 1, 0]]
print(solution2(land))

# print(solution([[0, 0, 0, 1, 1, 1, 1, 1],
#           [0, 0, 0, 0, 0, 0, 0, 1],
#            [1, 1, 1, 1, 1, 1, 1, 1],
#            [1, 1, 1, 0, 0, 0, 0, 0],
#            [1, 1, 1, 0, 0, 0, 1, 1]])) 
                    
            