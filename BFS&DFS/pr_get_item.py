from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX=102
    maps=[[-1]*MAX for i in range(MAX)]
    
    for retan in rectangle:
        x1,y1,x2,y2=map(lambda x: x*2,retan)
        
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    maps[i][j]=0
                elif maps[i][j]!=0:
                    maps[i][j]=1
  
    # 테두리 그리기 완료 - 테두리 그리는게 진짜 어려움. 테두리를 따라 이동해야하기 때문에 도형의 칸수 차이가 1이 나면 잘못된 경로로 갈 수 있음. 이걸 해결해준게 모든 좌표를 2배해준것. 겹치는 문제에서는 이런 아이디어가 필요할 듯.
    visited=[[0]*MAX for i in range(MAX)]
    queue=deque()
    queue.append((characterX*2,characterY*2))
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    while (queue):
        x,y=queue.popleft()
        if x==(itemX*2) and y==(itemY*2):
            break
        for cx,cy in zip(dx,dy):
            tmp_x=x+cx
            tmp_y=y+cy
            if 0<= tmp_x <= MAX and 0<= tmp_y<=MAX:
                if visited[tmp_x][tmp_y]==0 and maps[tmp_x][tmp_y]==1:
                    # 여기서 반드시 테두리인지를 확인해줘야함
                    visited[tmp_x][tmp_y]=visited[x][y]+1
                    queue.append((tmp_x,tmp_y))
    
    answer=visited[itemX*2][itemY*2]
    answer=answer//2
    return answer